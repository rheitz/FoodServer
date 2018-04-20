import RPi.GPIO as GPIO

# Setup GPIO (2-27)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
for i in range(2,21):
    GPIO.setup(i,GPIO.OUT)

def fanOn():
    GPIO.output(11, GPIO.HIGH)

def fanOff():
    GPIO.output(11, GPIO.LOW)

def humidifierFanOn():
    GPIO.output(12, GPIO.HIGH)

def humidifierFanOff():
    GPIO.output(12, GPIO.LOW)

def misterOn():
    GPIO.output(13, GPIO.HIGH)


def misterOff():
    GPIO.output(13, GPIO.LOW)

def lightsOn():
    lights = [27, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for pins in lights:
        GPIO.output(pins, GPIO.HIGH)


def lightsOff():
    lights = [27, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for pins in lights:
        GPIO.output(pins, GPIO.LOW)

def humidifierOn():
    mister.on()
    fan.on()

def humidifierOff():
    mister.off()
    fan.off()