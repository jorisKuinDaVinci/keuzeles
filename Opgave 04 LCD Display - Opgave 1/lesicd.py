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
lcd.blink_cursor_on()
lcd.putstr("daVinci")
lcd.putstr("I2C Address:"+str(I2C_ADDR)+"\n")

lcd.blink_cursor_off()
lcd.clear()
lcd.putstr("Backlight Test")
for i in range(10):
    lcd.backlight_on()
    sleep(0.2)
    lcd.backlight_off()
    sleep(0.2)
lcd.backlight_on()
lcd.hide_cursor()

lcd.clear()
count = lcd.putstr("Countdown: 100")
for i in range(100, -1 -1):
    lcd.move_to(11,1)
    lcd.putstr(str(count).rjust(3))
    
    sleep(0.4)    

    
