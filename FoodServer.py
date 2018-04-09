# Food Server
# Ideaventions Academy
# 7th Grade 2017-2018

# imports
import RPi.GPIO as GPIO
import time

# variables


# functions

# Turn on/off times for light
# Target temperature and humidity (76 F and 70% RH)
TIME_OFF = 21 # 9 pm at night turn off
TIME_ON = 6 # 6 am turn on
TEMP_FAN = 76 # temp F
# Max T
# Min T
# Max RH
# Min RH

# Setup GPIO (2-27)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
for i in range(2,21):
    GPIO.setup(i,GPIO.OUT)
GPIO.setup(22,GPIO.IN)  


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
