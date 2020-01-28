#!/usr/bin/Python

import RPi.GPIO as GPIO
import time
import sys

sys.path.append("/home/pi/code/Gardenpro/GardenYes/Scripts/modules")
import ADC0832_tmp
import lcd1602


def setup():

	ADC_CS  = 29
	ADC_CLK = 31
	ADC_DIO = 33
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ADC_CS, GPIO.OUT)
	GPIO.setup(ADC_CLK, GPIO.OUT)

def end():
	GPIO.cleanup()

def loop():
	while True:
		sig = ADC0832_tmp.getResult(0)
		GPIO.cleanup()
		lcd = lcd1602.Adafruit_CharLCD()
		lcd.clear()
		lcd.message("Soil moisture :")
		lcd.message(str(sig))
		time.sleep(1.0)

if(__name__ == '__main__'):
	setup()
	try:
		sig = ADC0832_tmp.getResult(0)
		GPIO.cleanup()

		lcd = lcd1602.Adafruit_CharLCD()
		lcd.clear()
		lcd.message("Soil moisture :")
		lcd.message(str(sig))

	except KeyboardInterrupt:
		end()


#GPIO SETUP
# channel = 37
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(channel, GPIO.IN)

# def callback(channel):
# 	if GPIO.input(channel):
# 	    print("no water detected")
# 	else:
# 	    print("water detected")

# GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) #let us know when the pin goes HIGH or LOW
# GPIO.add_event_callback(channel, callback) #assign function to GPIO PIN, run funcion on change

# #loop
# while True:
# 	time.sleep(1)
