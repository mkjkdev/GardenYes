#!/usr/bin/python

import mysql.connector
import config

mydb = mysql.connector.connect(
	host = "localhost"
	user = "root"
	passwd = "delical300"
)

print(mydb)
