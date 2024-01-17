from machine import Pin
from time import sleep

knop = Pin(15, Pin.IN)
led = Pin(6, Pin.OUT)
 
while True:
    if knop.value() == 1:
        for _ in range(10):
            led.on()
            sleep(0.3)
            led.off()
            sleep(0.3)