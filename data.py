import time
import busio
import board
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
from bmp280 import BMP280
from smbus2 import SMBus

# initialization of BMP 280
bus = SMBus(1)
sensor_bmp = BMP280(i2c_dev=bus)


# BOARD --> take the pysical numbers of the pin board
GPIO.setmode(GPIO.BCM)


# create i2c bus for soil measuring
i2c = busio.I2C(board.SCL, board.SDA)

# identified values of soil_value_ident.py
low_wather = 21866
high_wather = 8195

# define fuction to calculate the percent of the wather in soil
def soil(input_measured_value):
    if input_measured_value >= low_wather:
        return 0
    elif input_measured_value <= high_wather:
        return 100
    else:
        rangee = low_wather - high_wather
        wather_rel = input_measured_value - high_wather
        wather = wather_rel / rangee * 100
        return wather

    
# create object of ADC (Analog Digital Converter) using i2c bus
ads = ADS.ADS1115(i2c)

while True:
    
    try:
        # read values and voltage in the value variable
        value = AnalogIn(ads, ADS.P0)

        # measured_voltage= value.voltage
        # measured_voltage_in_percent = round(soil(measured_voltage), 2)

        measured_value= value.value
        measured_value_in_percent = round(soil(measured_value), 2)

        # print value and voltage in 1 secound interval
        # print(F'Wert: {format(value.value)}', F'Volt: {format(value.voltage)}')
        # print(F'{measured_voltage_in_percent} %')
        # print(F'{measured_value_in_percent} %')
    except:
        # measured_voltage_in_percent = 0
        measured_value_in_percent = 0
        print(F'{measured_value_in_percent} % as Error Value')
    
    # PIN 16 as input for the measuring of the watering system status ON of OFF
    try:
        GPIO.setup(16, GPIO.IN)
        system_status = GPIO.input(16)
        #print(GPIO.input(16), "Bewässerung aus")
    except:
        system_status = 1

    # read preassure and temperature with BMP 280
    try:
        preassure = sensor_bmp.get_pressure()
        temperature = sensor_bmp.get_temperature()
    except:
        preassure = 0
        temperature = 0

    
    print(F'{measured_value_in_percent} % System Status: {system_status} Temperature: {temperature} Preassure: {preassure}')
    time.sleep(1)    





# !!!!!!!!!!!!!!!!!!! create post request to influxDB !!!!!!!!!!!!!!!!!!!!!!

