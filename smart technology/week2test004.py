from machine import Pin
from time import sleep
PIN = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
hoeveel_leds = int(input(f"hoeveel leds moeten aaangezet worden?"))
if hoeveel_leds in PIN:
    print(f"deze leds worden nu aangezet")
else:
    print(f"Deze leds kan ik niet vinden")
pin = []
for id in PIN:
    pin.append(Pin(id, Pin.OUT))

for led in pin:    
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)