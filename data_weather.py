import time
import bme280
from smbus2 import SMBus

# initialization of BME 280
bus = SMBus(1)
address = 0x76
calibration_params = bme280.load_calibration_params(bus, address)


while True:
    # read preassure and temperature with BMP 280
    try:
        data = bme280.sample(bus, address, calibration_params)
        pressure = round(data.pressure, 3)
        temperature = round(data.temperature, 3)
        humidity = round(data.humidity, 3)
    except:
        pressure = 0
        temperature = 0
        humidity = 0
    
    print(F'Temperature: {temperature} Preassure: {pressure} Humidity: {humidity}')
    time.sleep(1)


    # !!!!!!!!!!!!!!!!!!! create post request to influxDB !!!!!!!!!!!!!!!!!!!!!!


    