import busio
import board
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
import time
import statistics


# BCM --> take the numbers of the pins like on the raspberry plan
GPIO.setmode(GPIO.BCM)

# # create i2c bus
i2c = busio.I2C(board.SCL, board.SDA)

# create object of ADC (Analog Digital Converter) using i2c bus
ads = ADS.ADS1115(i2c)

# identified values of soil_value_ident.py
low_wather = 21866
high_wather = 8195

# define the wathering time if the wathering system is in progress --> in scounds
wathering_time = 5

# define wather effekt time if the wathering process is finish --> in secounds
effect_time = 10

# define the value wich is responsible to set the trigger on GO --> in percent of soil condition
set_trigger = 20

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


while True:

    # create lis to calculate mean value of the readed values
    trigger_list = []
    # set the loop counter on 0 for 10 interations
    counter = 0

    while counter < 20:
        
        try:
            # read values and voltage in the value variable
            value = AnalogIn(ads, ADS.P0)

            # read values and voltage in the value variable
            measured_value= value.value
            measured_value_in_percent = round(soil(measured_value), 2)
            # y = round(soil(voltage), 2)
        except:
            measured_value_in_percent = 100
        
        trigger_list.append(measured_value_in_percent)
        # print(trigger_list)
        # print(F'Average: {statistics.mean(trigger_list)}')
        time.sleep(0.5)
        counter += 1

    trigger_value = statistics.mean(trigger_list)
    
    # temporary exit point to develop trigger value
    # import sys
    # sys.exit()


    # !!!!!!!!!!!!!!!!! Start the wathering system !!!!!!!!!!!!!!!!!!!!!!!

    if trigger_value < set_trigger:

    

        # PIN 36 as input for the measuring of the watering system status ON of OFF
        # GPIO.setup(16, GPIO.IN)
        # print(GPIO.input(16), "Bewässerung aus")
        # time.sleep (2)

        try:
            # PIN 37 set OUT, if the wathering system have to start the wathering
            GPIO.setup(26, GPIO.OUT)
            # print('wathering in progress.......')

            # define the acitve wathering time in secounds
            time.sleep(wathering_time)
            # PIN 37 set IN, if the wathering system habe to stop
            GPIO.setup(26, GPIO.IN)
            time.sleep(effect_time)
            # print('wathering system going to off......')
            
            #GPIO.output(26, False)
        except:
            GPIO.setup(26, GPIO.IN)
