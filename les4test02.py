from machine import Pin
from time import sleep

knop_blauw = Pin(28, Pin.IN)

teller = 0
while True:
    sleep(1)
    waarde = knop_blauw.value() == 1
    print(teller, waarde)
    teller += 1