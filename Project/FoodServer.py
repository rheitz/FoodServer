# Food Server
# Ideaventions Academy
# 7th Grade 2017-2018

# imports
import time
from Project.Functions import *

# variables

# Turn on/off times for light
# Target temperature and humidity (76 F and 70% RH)
TEMP_FAN = 76
TIME_OFF = 21  # 9 pm at night turn off
TIME_ON = 6  # 6 am turn on
MAX_TEMP = 76  # Max T
MIN_TEMP = 63  # Min T
TARGET_TEMP = 72
MAX_RH = 50  # Max RH
MIN_RH = 17  # Min RH
TARGET_RH = 40
LightsAreOn = False
FanIsOn = False
HumidifierIsOn = False
temperature = 0
humidity = 0

# Main loop
# Get time and see if lights should be on or off
while True:
    time = time.localtime()
    if LightsAreOn == False and time.tm_hour == TIME_ON:
        lightsOn()
        LightsAreOn = True
    if LightsAreOn == True and time.tm_hour == TIME_OFF:
        lightsOff()
        LightsAreOn = False
    if FanIsOn == False and temperature >= MAX_TEMP:
        fanOn()
        FanIsOn = True
    if FanIsOn == True and temperature <= TARGET_TEMP:
        fanOff()
        FanIsOn = False
    if HumidifierIsOn == False and humidity <= MIN_RH:
        humidifierOn()
        HumidifierIsOn = True
    if HumidifierIsOn == True and humidity >= TARGET_RH:
        humidifierOff()
        HumidifierIsOn = False

