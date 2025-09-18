import time
import busio
import board
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# create i2c bus
i2c = busio.I2C(board.SCL, board.SDA)

# !!!!!!!!!!!!!!! This values based on voltage output !!!!!!!!!!!!!!!!!!!!!!!!
# low_wather == 2,733 --> out of wather 0%
# high wather == 1,02 --> in wather 100%

# low_wather = 2.733
# high_wather = 1.02

# !!!!!!!!!!!!!!! This values based on calculated value output !!!!!!!!!!!!!!!!!!!!!!!!
# low_wather == max:21866 --> out of wather 0%
# high wather == min:8195   --> in wather 100%

# create object of ADC (Analog Digital Converter) using i2c bus
ads = ADS.ADS1115(i2c)

while True:

     # read values and voltage in the value variable
    value = AnalogIn(ads, ADS.P0)

    print(F'Wert: {format(value.value)}', F'Volt: {format(value.voltage)}')

    time.sleep(1)


