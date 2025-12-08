# watering_system

## description

# Hardware Componets

# Load new system on raspberry pi

<b>Initial Commands:</b>
apt-get update
apt-get upgrade -y --> everthing is YES
raspi-config --> set i2c bus enable
raspi-config --> set the correct timezone of your country (Europe/Vienna)

<b>Install Docker:</b>
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
docker run hello-world

<b>Create .env File in Project directory --> touch .env</b>
INFLUX_USER = ''
INFLUX_PASSWORD = ''
HOST = 'LOCALUSER-OR-IP'
INFLUX_PORT = 
INFLUX_DATABASE = ''


## Create Influx Database

1. open shell and directed into project order
2. shell command: docker excec -it influxdb influx
3. shell command: create databases <NAMEDATABASE> --> type NAMEDATABASE also in .env File in Line INFLUX_DATABASE as string
4. shell command: exit
