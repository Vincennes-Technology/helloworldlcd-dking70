#!/usr/bin/python
#show "Hello World on the LCD screen"
# DKing

import Adafruit_CharLCD as LCD
import time
import subprocess

lcd = LCD.Adafruit_CharLCDPlate()

displayText = "Hello World\n"
displayText = "Hello World"

lcd.clear()
lcd.message(displayText)
Name = subprocess.check_output(['hostname']).strip()
IPaddr = subprocess.check_output(['hostname', '-I'])
displayText2 = IPaddr + Name

lcd.clear()
lcd.set_backlight(1)
refresh = True
while (True):
    if lcd.is_pressed(LCD.SELECT):
        lcd.clear()
        lcd.message(displayText)
        refresh = True

    else:
        if refresh:
            lcd.set_backlight(1)
            lcd.clear()
            lcd.message(displayText2)
            refresh = False
time.sleep(0.5)