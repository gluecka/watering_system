# watering_system

## description

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

## Start Docker services

shell command: docker compose up -d<br>

## Create Influx Database

1. open shell and directed into project order
2. shell command: docker excec -it influxdb influx
3. shell command: create database <NAMEDATABASE> --> type NAMEDATABASE also in .env File in Line INFLUX_DATABASE as string
4. shell command: exit
