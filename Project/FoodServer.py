# Food Server
# Ideaventions Academy
# 7th Grade 2017-2018
# imports
import time
import Project.Functions

# variables

# Turn on/off times for light
# Target temperature and humidity (76 F and 70% RH)
TIME_OFF = 21
TIME_ON = 6
TEMP_FAN = 76
LightsAreOn = False
TIME_OFF = 21 # 9 pm at night turn off
TIME_ON = 6 # 6 am turn on
MAX_TEMP = 76 # Max T
MIN_TEMP = 63 # Min T
TARGET_TEMP = 72
MAX_RH = 50 # Max RH
MIN_RH = 17 # Min RH
TARGET_RH = 40




# Main loop
# Get time and see if lights should be on or off
while True:
    time = time.localtime()
    if LightsAreOn == False and time.tm_hour == TIME_ON:
        Funcions
        LightsAreOn = True
    if LightsAreOn == True and time.tm_hour == TIME_OFF:
        lights.off()
        LightsAreOn = False
    if FanIsOn = False and temperature >= MAX_TEMP:
        fan.on()
        FanIsOn = True
    if FanIsOn = True and temperature <= TARGET_TEMP:
        fan.off()
        FanIsOn = False
    if HumidifierIsOn = False and humidity <= MIN_RH:
        humidifierControl(True)
        HumidifierIsOn = True
    if HumidifierIsOn = True and humidity >= TARGET_RH:
        humidifierControl(False)
        HumidifierIsOn = False
    
