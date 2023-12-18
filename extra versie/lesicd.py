from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
from time import sleep
import math
NUMBER_OF_ROWS = 2
NUMBER_OF_COLUMNS = 16

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = 39 #vul hier adres in
lcd = I2cLcd(i2c, I2C_ADDR, NUMBER_OF_ROWS, NUMBER_OF_COLUMNS)

lcd.clear()
lcd.blink_cursor_off()
lcd.hide_cursor()
count = lcd.putstr("Countdown: ")
for i in range(100, -1, -1):
    print(i)
    lcd.move_to(11,0)
    lcd.putstr(str(i) + "  ")
    sleep(0.1)