import time
import busio
import board
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# create i2c bus
i2c = busio.I2C(board.SCL, board.SDA)

# high voltage == 2,71 --> out of wather 0%
# low voltage == 1,006 --> in wather 100%

# define fuction to calculate the percent of the wather in soil
def soil(x):
    low_wather = 2.71
    high_wather = 1.006
    if x >= low_wather:
        return 0
    elif x <= high_wather:
        return 100
    else:
        rangee = low_wather - high_wather
        wather_rel = x - high_wather
        wather = wather_rel / rangee * 100
        return wather

    



# create object of ADC (Analog Digital Converter) using i2c bus
ads = ADS.ADS1115(i2c)

while True:
    # read values and voltage in the value variable
    value = AnalogIn(ads, ADS.P0)
    voltage= value.voltage
    y = round(soil(voltage), 2)

    # print value and voltage in 1 secound interval
    # print(F'Wert: {format(value.value)}', F'Volt: {format(value.voltage)}')
    print(F'{y} %')
    time.sleep(1)

