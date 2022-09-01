import telegram
import emaillib
import busio
import board
import adafruit_tmp117
i2c = busio.I2C(board.SCL, board.SDA)
tmp117 = adafruit_tmp117.TMP117(i2c)

if tmp117.temperature >= 8:
    emaillib.yagSend("Warning! Fridge too hot", "<img src='https://i.imgur.com/Wfyj5KV.jpg'><p>Current Temperature = {}".format(round(tmp117.temperature, 3)))
    telegram.sendtext("""Warning! Fridge too hot
Current Temperature = {}""".format(round(tmp117.temperature, 3)))
if tmp117.temperature <= 2:
    emaillib.yagSend("Warning! Fridge too cold", "<img src='https://i.imgur.com/vNCAERy.png'><p>Current Temperature = {}".format(round(tmp117.temperature, 3)))
    telegram.sendtext("""Warning! Fridge too cold
Current Temperature = {}""".format(round(tmp117.temperature, 3)))
