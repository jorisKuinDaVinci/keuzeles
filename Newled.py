from machine import Pin
from time import sleep
PIN = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)



pin = []
for id in PIN:
    pin.append(Pin(id, Pin.OUT))
print(pin)

while True:
    for led in pin:
            led.on()
            sleep(0.2)
            led.off()
            sleep(0.2)