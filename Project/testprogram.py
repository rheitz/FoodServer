import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(27)
for i in range(2,11):
    GPIO.setup(i,GPIO.OUT)

lights = [27,2,3,4,5,6,7,8,9,10]
for pins in lights:
    GPIO.output(pins,GPIO.HIGH)

sleep(10)

lights = [27,2,3,4,5,6,7,8,9,10]
for pins in lights:
    GPIO.output(pins,GPIO.LOW)
