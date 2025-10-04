# library RPi.GPIO habe to install directly on docker not as python venv
import busio
import board
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
import time
import statistics

# # !!!!!!!!!!!!!! define trigger condition !!!!!!!!!!!!!!!!!!!!!!

# # create i2c bus
# i2c = busio.I2C(board.SCL, board.SDA)

# # low_wather == 2,71 --> out of wather 0%
# # high wather == 1,006 --> in wather 100%

# # define fuction to calculate the percent of the wather in soil
# def soil(x):
#     low_wather = 2.71
#     high_wather = 1.006
#     if x >= low_wather:
#         return 0
#     elif x <= high_wather:
#         return 100
#     else:
#         rangee = low_wather - high_wather
#         wather_rel = x - high_wather
#         wather = wather_rel / rangee * 100
#         return wather

    
# # create object of ADC (Analog Digital Converter) using i2c bus
# ads = ADS.ADS1115(i2c)

# # create lis to calculate mean value of the readed values
# trigger_list = []
# # set the loop counter on 0 for 10 interations
# counter = 0

# while counter < 10:

#     # read values and voltage in the value variable
#     value = AnalogIn(ads, ADS.P0)
#     voltage= value.voltage
#     y = round(soil(voltage), 2)

    
#     trigger_list.append(y)
#     print(trigger_list)
#     print(statistics.mean(trigger_list))
#     time.sleep(1)
#     counter += 1

# # temporary exit point
# import sys
# sys.exit()


# !!!!!!!!!!!!!!!!! Start the wathering system !!!!!!!!!!!!!!!!!!!!!!!

# BOARD --> take the pysical numbers of the pin board
GPIO.setmode(GPIO.BCM)

# PIN 36 as input for the measuring of the watering system status ON of OFF
GPIO.setup(16, GPIO.IN)
print(GPIO.input(16), "Bewässerung aus")
time.sleep (2)

# PIN 37 set OUT, if the wathering system have to start the wathering
GPIO.setup(26, GPIO.OUT)
print(GPIO.input(16), 'Bewässerung gestartet')


#GPIO.output(26, True)

time.sleep (2)
# PIN 37 set IN, if the wathering system habe to stop
GPIO.setup(26, GPIO.IN)
print(GPIO.input(16), 'Bewässerung aus')

#GPIO.output(26, False)