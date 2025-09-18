import time
import busio
import board
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO

# !!!!!!!!!!!!!!!!!! measure the soil condition !!!!!!!!!!!!!!!!!!!!!!!!

# create i2c bus
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
        print(F'{measured_value_in_percent} %')
    except:
        # measured_voltage_in_percent = 0
        measured_value_in_percent = 0
        print(F'{measured_value_in_percent} % as Error Value')
    
    


# !!!!!!!!!!!!!!!!!!!! measure the temperature outside !!!!!!!!!!!!!!!!!!!!!!!



# !!!!!!!!!!!!!!!!!!! measure the on/off status of the wathering system !!!!!!!!!!!!!!!!!!

    # BOARD --> take the pysical numbers of the pin board
    # GPIO.setmode(GPIO.BOARD)

    # PIN 36 as input for the measuring of the watering system status ON of OFF
    GPIO.setup(27, GPIO.IN)
    status_watheringsystem = GPIO.input(27)
    if status_watheringsystem == 1:
        print("Bewässerung an")
    else:
        print('Bewässerung aus')
    
    time.sleep(1)



# !!!!!!!!!!!!!!!!!!! create post request to influxDB !!!!!!!!!!!!!!!!!!!!!!

