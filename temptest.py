import busio
import board
import adafruit_tmp117
i2c = busio.I2C(board.SCL, board.SDA)
tmp117 = adafruit_tmp117.TMP117(i2c)

print(tmp117.temperature)
