from machine import Pin
from time import sleep

PIN = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

knop_zwart = Pin(28, Pin.IN)

teller = 0
stand_oud = False
while True:
    sleep(0.1)
    stand_nu = knop_zwart.value() == 1
    if stand_nu and stand_oud == False:
        teller += 1
        print(teller)
    stand_oud = stand_nu
    
pin = []
for id in PIN:
    pin.append(Pin(id, Pin.OUT))

teller = 0
while True:
    for led in pin:
        led.on()
        sleep(0.2)
        led.off()
        sleep(0.2)
        teller += 1
    pin.reverse()



