from machine import Pin
from time import sleep
PIN_PICO = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29)

pin = []
for id in PIN_PICO:
    pin.append(Pin(id, Pin.OUT))

aantal_aan = int(input("Hoeveel leds wil je aanzetten 0...29 :"))
teller = 0
while teller < len(pin):
    if teller < aantal_aan:
        pin[teller].on()
    else:
        pin[teller].off()
    teller += 1
    