# library RPi.GPIO habe to install directly on docker not as python venv
import RPi.GPIO as GPIO
from time import sleep

# BOARD --> take the pysical numbers of the pin board
GPIO.setmode(GPIO.BOARD)

# PIN 36 as input for the measuring of the watering system status ON of OFF
GPIO.setup(36, GPIO.IN)
print(GPIO.input(36), "Bewässerung aus")
sleep (2)

# PIN 37 set OUT, if the wathering system have to start the wathering
GPIO.setup(37, GPIO.OUT)
print(GPIO.input(36), 'Bewässerung gestartet')


#GPIO.output(26, True)

sleep (2)
# PIN 37 set IN, if the wathering system habe to stop
GPIO.setup(37, GPIO.IN)
print(GPIO.input(36), 'Bewässerung aus')

#GPIO.output(26, False)









