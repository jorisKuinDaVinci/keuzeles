from machine import Pin
from utime import sleep

PINNEN = (3,4)
pin = []
for id in PINNEN:
    pin.append(Pin(id, Pin.OUT))

for led in pin:
  for i in range(10):
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
  