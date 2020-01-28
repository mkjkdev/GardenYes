#!/usr/bin/python

import Adafruit_DHT
import time

import sys
sys.path.append("/home/pi/code/Gardenpro/GardenYes/Scripts/modules")
import lcd1602


def getData():
	sensor = Adafruit_DHT.DHT11
	pin = 4
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	return(temperature, humidity)

def LCD(temperature, humidity):
	lcd.clear()
	lcd.message("Temperature : ")
	lcd.message(str(temperature))
	time.sleep(2.0)
	lcd.clear()

	lcd.message("Humidity : ")
	lcd.message(str(humidity))
	time.sleep(2.0)
	lcd.clear()
