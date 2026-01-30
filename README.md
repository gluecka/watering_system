# Watering and Weather System

## Description based on a Raspberry PI 3<br>

# Hardware Componets

1. soil measuring: Capacitive Soil Moisture Sensor v1.2
2. ADC Modul for soil measuring connection: ARCELI 16 Bit 16 Byte 4-Channel I2C
3. BME 280 5V

# Load new system on raspberry pi

<b>Initial Commands:</b> <br>
apt-get update <br>
apt-get upgrade -y --> everthing is YES <br>
raspi-config --> set i2c bus enable<br>
raspi-config --> set the correct timezone of your country (Europe/Vienna)<br><br>

<b>Install Docker:</b>
curl -fsSL https://get.docker.com -o get-docker.sh<br>
sudo sh get-docker.sh<br>
sudo usermod -aG docker $USER<br>
docker run hello-world<br><br>

<b>Create .env File in Project directory --> touch .env</b>
INFLUX_USER = ''<br>
INFLUX_PASSWORD = ''<br>
HOST = 'LOCALUSER-OR-IP'<br>
INFLUX_PORT = <br>
INFLUX_DATABASE = ''<br>

## External Network for NGINX Webserver

shell command: docker network create nginx-Proxy<br><br>

## Create directory of Volumes

shell command: mkdir Docker_volumes --> in project order<br>
shell command: chmod 777 Docker_volumes<br><br>

## Calibration of the soil sensor:

Open directory --> Calibration<br>
shell command: ./build.sh --> once only<br>
shell command: ./deploy_container.sh<br>
shell command: docker exec -it soil_ident /bin/bash<br>
shell command in docker shell: python soil_value_ident.py<br>
1. write down the value if the sensor is out of wather
2. write down the value if the sonsor is complet in wather
shell command: exit<br>
shell command: docker kill soil_ident & docker rm soil_ident<br><br>


# Define this values in the files: trigger.py; data_wathering.py
write the measured value of the sensor out of wather in the variable low_wather<br>
write the measrued value of the sonsor complet in wather in the variable high_wather<br><br>

# Build new docker image about the new sensor values
shell command: docker compose -f docker-compose.service.yml build py-trigger<br>
shell command: docker compose -f docker-compose.service.yml build data-wathering<br><br>

<b>And then start the docker service like in the description "Start Docker services"</b><br><br>


## Start Docker services

shell command: docker compose -f docker-compose.service.yml up -d<br>
shell command: docker compose -f docker-compose.web.yml up -d<br><br>

## Create Influx Database

1. open shell and directed into project order
2. shell command: docker excec -it influxdb influx
3. shell command: create database <NAMEDATABASE> --> type NAMEDATABASE also in .env File in Line INFLUX_DATABASE as string
4. shell command: exit
