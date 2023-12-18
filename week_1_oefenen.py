from machine import Pin
from time import sleep

PIN = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

pin = []

knop_blauw = Pin(28, Pin.IN)

for id in PIN:
    pin.append(Pin(id, Pin.OUT))
    
teller = 0
while True:
    waarde = knop_blauw.value() == 1
    print(waarde)
    if waarde == True:
        for led in pin:
            led.on()
            sleep(0.2)
            led.off()
            sleep(0.2)
            teller += 1


# led_1 = Pin(0, Pin.OUT)
# led_2 = Pin(1, Pin.OUT)
# led_3 = Pin(2, Pin.OUT)
# led_4 = Pin(3, Pin.OUT)
# led_5 = Pin(4, Pin.OUT)
# led_6 = Pin(5, Pin.OUT)
# led_7 = Pin(6, Pin.OUT)
# led_8 = Pin(7, Pin.OUT)
# led_9 = Pin(8, Pin.OUT)
# led_10 = Pin(9, Pin.OUT)
# led_11 = Pin(10, Pin.OUT)
# led_12 = Pin(11, Pin.OUT)
# led_13 = Pin(12, Pin.OUT)
# led_14 = Pin(13, Pin.OUT)
# led_15 = Pin(14, Pin.OUT)
# led_16 = Pin(15, Pin.OUT)
# TIME_SLEEP = .1 #1 seconde
# 
# i = 10
# while i > 0:
#     led_1.on()
#     sleep(TIME_SLEEP)
#     led_1.off()
#     sleep(TIME_SLEEP)
#     led_2.on()
#     sleep(TIME_SLEEP)
#     led_2.off()
#     sleep(TIME_SLEEP)
#     led_3.on()
#     sleep(TIME_SLEEP)
#     led_3.off()
#     sleep(TIME_SLEEP)
#     led_4.on()
#     sleep(TIME_SLEEP)
#     led_4.off()
#     sleep(TIME_SLEEP)
#     led_5.on()
#     sleep(TIME_SLEEP)
#     led_5.off()
#     sleep(TIME_SLEEP)
#     led_6.on()
#     sleep(TIME_SLEEP)
#     led_6.off()
#     sleep(TIME_SLEEP)
#     led_7.on()
#     sleep(TIME_SLEEP)
#     led_7.off()
#     sleep(TIME_SLEEP)
#     led_8.on()
#     sleep(TIME_SLEEP)
#     led_8.off()
#     sleep(TIME_SLEEP)
#     led_9.on()
#     sleep(TIME_SLEEP)
#     led_9.off()
#     sleep(TIME_SLEEP)
#     led_10.on()
#     sleep(TIME_SLEEP)
#     led_10.off()
#     sleep(TIME_SLEEP)
#     led_11.on()
#     sleep(TIME_SLEEP)
#     led_11.off()
#     sleep(TIME_SLEEP)
#     led_12.on()
#     sleep(TIME_SLEEP)
#     led_12.off()
#     sleep(TIME_SLEEP)
#     led_13.on()
#     sleep(TIME_SLEEP)
#     led_13.off()
#     sleep(TIME_SLEEP)
#     led_14.on()
#     sleep(TIME_SLEEP)
#     led_14.off()
#     sleep(TIME_SLEEP)
#     led_15.on()
#     sleep(TIME_SLEEP)
#     led_15.off()
#     sleep(TIME_SLEEP)
#     led_16.on()
#     sleep(TIME_SLEEP)
#     led_16.off()
#     i -= 1
#     
    



