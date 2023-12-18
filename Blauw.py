from machine import Pin
from time import sleep

knop_rood = Pin(28, Pin.IN)

teller = 0
while True:
    sleep(1)
    waarde = knop_rood.value() == 1)
    teller += 1