from machine import Pin
from time import sleep
PIN = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

pin = []
for id in PIN:
    pin.append(Pin(id, Pin.OUT))

aantal_aan = int(input("Hoeveel leds wil je aanzetten 0...15 :"))
teller = 0
for index in range (len(pin)+1):    
    led.on()
    
    led.off()
    