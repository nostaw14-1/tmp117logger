from influxdb import InfluxDBClient
import datetime
client=InfluxDBClient(host="localhost",port="8086")
from time import *
import time
import board
import busio
import adafruit_tmp117

i2c = busio.I2C(board.SCL, board.SDA)
tmp117 = adafruit_tmp117.TMP117(i2c)

import pytz
#client.create_database("MyDatabase")
print(client.get_list_database())
client.switch_database('test')

while True:
    

    json_body = [
    {
        "measurement": "TMP117",
        "tags": {
            "requestName": "LaunchURL",
            "requestType": "GET"
                },
        "time":datetime.datetime.now(tz=pytz.UTC),
         "fields": {
            "Temperature": tmp117.temperature,
                    }
        },

    ]

client.write_points(json_body)
results=client.query('SELECT * FROM NewResponse')
login_points=list(results.get_points(measurement='NewResponse',tags={"requestName": "Login"}))

