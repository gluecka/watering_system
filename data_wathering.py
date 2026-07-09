import time
import busio
import board
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
from influxdb import InfluxDBClient
from datetime import datetime
import statistics
import os
from dotenv import load_dotenv
load_dotenv()
from models import SensorValueTrasformator


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


while True:
    
    try:
        measure_list = []

        for x in range(6):
            # read values and voltage in the value variable
            sensor_output = AnalogIn(ads, ADS.P0)

            # measured_voltage= value.voltage
            # measured_voltage_in_percent = round(soil(measured_voltage), 2)

            measured_value= sensor_output.value
            # define Object to transform the sensor value into percent
            measured_value_in_percent = SensorValueTrasformator(measured_value)

            measure_list.append(measured_value_in_percent.percent_calculation())
            time.sleep(0.5)

        measured_value_in_percent = float(statistics.mean(measure_list))

    except:
        measured_value_in_percent = float(0.0)
        # print(F'{measured_value_in_percent} % as Error Value')
    
    # PIN 16 as input for the measuring of the watering system status ON of OFF
    try:
        GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        system_status = GPIO.input(16)
    except:
        system_status = 1
        
    # print(F'Bodenfeuchte: {measured_value_in_percent} % System Status: {system_status}') # --> dev
    # print(type(measured_value_in_percent)) # --> dev
    # time.sleep(2) # --> dev

    # # temporary exit point to develop trigger value
    # import sys # --> dev
    # sys.exit() # --> dev

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
    
