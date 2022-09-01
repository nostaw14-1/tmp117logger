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
print(client.get_list_database())
client.switch_database('tmp117realtime')

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
    time.sleep(5)
