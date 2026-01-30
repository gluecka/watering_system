import time
import bme280
from smbus2 import SMBus
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
        pressure = 0.0
        temperature = 0.0
        humidity = 0.0
    
    # print(F'Temperature: {temperature} Preassure: {pressure} Humidity: {humidity}')
    


    # !!!!!!!!!!!!!!!!!!! create post request to influxDB !!!!!!!!!!!!!!!!!!!!!!

    # set influx client
    client = InfluxDBClient(HOST, PORT, USER, PASSWORD, DATABASE)

    json_payload = []

    data_1 = {
        'measurement' : 'weather',
        'time' : datetime.now(),
        'fields' : {
        'Temperatur' : temperature,
        'Luftfeuchtigkeit' : humidity,
        'Luftdruck' : pressure
            }
    }

    json_payload.append(data_1)

    # write data in influxdb
    client.write_points(json_payload)
    time.sleep(2)
    #print(json_payload)
