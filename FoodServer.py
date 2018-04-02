# Food Server
# Team Mac and Cheese
#

# imports
import RPi.GPIO as GPIO
import time

# variables


# functions

# Turn on/off times for light
# Target temperature and humidity (76 F and 70% RH)
TIME_OFF = 21
TIME_ON = 6
TEMP_FAN = 76
# Setup GPIO (2-27)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
for i in range(2,21):
    GPIO.setup(i,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)



# Main loop
# Get time and see if lights should be on or off
while True:
    time = time.localtime()
    if time.tm_hour == TIME_ON:
        lights.on()
    if time.tm_hour == TIME_OFF:
        lights.off()
    if temperature >= TEMP_FAN:
        fan.on()
    else:
        fan.off()
