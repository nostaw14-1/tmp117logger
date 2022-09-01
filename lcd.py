import time
import I2C_LCD_driver
import board
import busio
import fontdata
import adafruit_tmp117
lcd = I2C_LCD_driver.lcd()
i2c = busio.I2C(board.SCL, board.SDA)
tmp117 = adafruit_tmp117.TMP117(i2c)
lcd.lcd_clear() 
lcd.lcd_display_string("Fridge Temp  C", 1, 1)

while True:
    lcd.lcd_display_string("{}  ".format(round(tmp117.temperature, 3)), 2, 5)
    lcd.lcd_load_custom_chars(fontdata.fontdata)
    lcd.lcd_write(0x8D)
    lcd.lcd_write_char(0)
    time.sleep(1)
