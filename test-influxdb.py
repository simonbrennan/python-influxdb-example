#!/usr/bin/python
'''
Simple influxdb client code that pushes random values into the DB at 1 minute intervals.
'''

from influxdb import client as influxdb
import time
import random

host='localhost'
port = 8086
user = "root"
password = "root"
db_name = "hello_world"
db = influxdb.InfluxDBClient(host, port, user, password, db_name)

db.create_database(db_name)

while True: 
	json_body = [
	        {
	            "measurement": "bandwidth",
	            "tags": {
	                "host": "localhost",
	                "object": "services"
	            },
	            "fields": {
	                "speed_in": random.randrange(10000000,500000000,10000),
	                "speed_out": random.randrange(10000000,500000000,10000)
	            }
	        }
	    ]

	db.write_points(json_body)
	series = db.query("show series;")
	print "series: {0}".format(series)
        time.sleep(60)
# To see pretty things log in to your influxdb UI (probably http://localhost:8083/) and run a query like `select * from foo`
