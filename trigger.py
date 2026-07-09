import busio
import board
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
import time
import statistics
from models import SensorValueTrasformator
import json

# read config.json File
with open('config.json', 'r') as f:
    config = json.load(f)

# BCM --> take the numbers of the pins like on the raspberry plan
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)

# # create i2c bus
i2c = busio.I2C(board.SCL, board.SDA)

# create object of ADC (Analog Digital Converter) using i2c bus
ads = ADS.ADS1115(i2c)

while True:

    # create lis to calculate mean value of the readed values
    trigger_list = []

    for x in range(config['loop_counter_limit']):
        
        try:
            # read values and voltage in the value variable
            sensor_output = AnalogIn(ads, ADS.P0)

            # read values and voltage in the value variable
            measured_value= sensor_output.value
            # define Object to transform the sensor value into percent
            measured_value_in_percent = SensorValueTrasformator(measured_value)

        except:
            measured_value_in_percent = SensorValueTrasformator(config['high_wather'])
        
        trigger_list.append(measured_value_in_percent.percent_calculation())
        # print(trigger_list) # --> dev
        # print(F'Average: {statistics.mean(trigger_list)}') # --> dev
        time.sleep(0.5)

    trigger_value = statistics.mean(trigger_list)
    
    # temporary exit point to develop trigger value # --> dev
    # import sys # --> dev
    # sys.exit() # --> dev


    # !!!!!!!!!!!!!!!!! Start the wathering system !!!!!!!!!!!!!!!!!!!!!!!

    if trigger_value < config['trigger_limit']:

        try:
            # PIN 37 set OUT, if the wathering system have to start the wathering
            GPIO.setup(26, GPIO.OUT)
            # print('wathering in progress.......')

            # define the acitve wathering time in secounds
            time.sleep(config['wathering_time'])

            # PIN 37 set IN, if the wathering system have to stop
            GPIO.setup(26, GPIO.IN)

            time.sleep(config['effect_time'])
            # print('wathering system going to off......')

        except:
            GPIO.setup(26, GPIO.IN)
