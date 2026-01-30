import time
import busio
import board
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
from influxdb import InfluxDBClient
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

#import from .env File
USER = os.environ.get('INFLUX_USER')
PASSWORD = os.environ.get('INFLUX_PASSWORD')
HOST = os.environ.get('HOST')
DATABASE = os.environ.get('INFLUX_DATABASE')
PORT = os.environ.get('INFLUX_PORT')

# BOARD --> take the pysical numbers of the pin board
GPIO.setmode(GPIO.BCM)

# create i2c bus for soil measuring
i2c = busio.I2C(board.SCL, board.SDA)

# create object of ADC (Analog Digital Converter) using i2c bus
ads = ADS.ADS1115(i2c)

# identified values of soil_value_ident.py
# write the value in the variable--> low_wather if the sensor is absolutely dry
# write the value in the variable--> high_wather if the sensor is in wather
low_wather = 22000
high_wather = 7900

# define fuction to calculate the percent of the wather in soil
def soil(input_measured_value):
    if input_measured_value >= low_wather:
        return float(0.1)
    elif input_measured_value <= high_wather:
        return float(100.1)
    else:
#        rangee = low_wather - high_wather
#        wather_rel = (input_measured_value + 0.11111111) - high_wather
#        wather = wather_rel / rangee * 100
        gradient = -100 / low_wather
        wather = gradient * input_measured_value + 100
        return float(wather)

while True:
    
    try:
        # read values and voltage in the value variable
        value = AnalogIn(ads, ADS.P0)

        # measured_voltage= value.voltage
        # measured_voltage_in_percent = round(soil(measured_voltage), 2)

        measured_value= value.value
        measured_value= float(measured_value)
        # measured_value_in_percent = round(soil(measured_value), 2)
        measured_value_in_percent = soil(measured_value)

        # print value and voltage in 1 secound interval
        # print(F'Wert: {format(value.value)}', F'Volt: {format(value.voltage)}')
        # print(F'{measured_voltage_in_percent} %')
        # print(F'{measured_value_in_percent} %')
    except:
        # measured_voltage_in_percent = 0
        measured_value_in_percent = float(0.0)
        # print(F'{measured_value_in_percent} % as Error Value')
    
    # PIN 16 as input for the measuring of the watering system status ON of OFF
    try:
        GPIO.setup(16, GPIO.IN)
        system_status = GPIO.input(16)
        # print(GPIO.input(16), "Bewässerung aus")
    except:
        system_status = 1
        

    
#    print(F'Bodenfeuchte: {measured_value_in_percent} % System Status: {system_status}')
#    print(type(measured_value_in_percent))
#    time.sleep(2)    

    # # temporary exit point to develop trigger value
    # import sys
    # sys.exit()



# !!!!!!!!!!!!!!!!!!! create post request to influxDB !!!!!!!!!!!!!!!!!!!!!!

    # set influx client
    client = InfluxDBClient(HOST, PORT, USER, PASSWORD, DATABASE)

    json_payload = []

    data_1 = {
        'measurement' : 'wathering',
        'time' : datetime.now(),
        'fields' : {
            'Bodenfeuchtigkeit' : measured_value_in_percent,
            'Status Bewässerung' : system_status
        }
    }

    json_payload.append(data_1)

    # write data in influxdb
    client.write_points(json_payload)
#    print(json_payload)
    time.sleep(2)
    
