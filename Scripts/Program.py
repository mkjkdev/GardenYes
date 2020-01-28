#!/usr/bin/python
import time
import mysql.connector
import sys

sys.path.append("/home/pi/code/Gardenpro/GardenYes/Scripts/modules")
import Soil_
import Dht11_

#Main script, collect data and upload to sql


if(__name__ == "__main__"):
	while True:
		Soil_.setup()

		#Get data from DHT11 script and Soil script
		soil = Soil_.ADC0832_tmp.getResult(0)
		temperature, humidity = Dht11_.getData()

		#post to database
		try:
			conn = mysql.connector.connect(host="localhost", user="root",passwd="delical300",database="gardenpro")
			cursor = conn.cursor()

			sql = ("INSERT INTO garden (temperature, humidity, soil) VALUES (%s, %s, %s)")
			values = (temperature, humidity, soil)

			cursor.execute(sql, values)
			conn.close()
			time.sleep(60)
		except mysql.connector.Error as e:
			print(e)
