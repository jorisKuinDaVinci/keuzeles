from machine import Pin
from time import sleep
PIN = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
#PIN_WEMOS = (16,14,12,13,15)
pin = []
for id in PIN:
#for id in PIN_WEMOS:
    pin.append(Pin(id, Pin.OUT))

for led in pin:    
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)