import I2C_LCD_driver
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-1", "--lcdline1", required=True,
   help="First Line")
ap.add_argument("-2", "--lcdline2", default=" ", required=False,
   help="Second Line")
args = vars(ap.parse_args())
lcd = I2C_LCD_driver.lcd()
lcd.lcd_clear()
lcd.lcd_display_string(str(args["lcdline1"]), 1)
lcd.lcd_display_string(str(args["lcdline2"]), 2)

