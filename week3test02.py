from machine import Pin
from time import sleep
zzzzz = 1
led = Pin(28, Pin.OUT)

while True:
    led.on()
    sleep(zzzzz)
    led.off()
    sleep(zzzzz)