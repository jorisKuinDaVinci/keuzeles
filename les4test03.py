from machine import Pin
from time import sleep

knop_blauw = Pin(28, Pin.IN)
knop_rood = Pin(27, Pin.IN)
teller = 0
PINNEN = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
pin = []

led_index = 0

while True:
    sleep(0.2)
    waarde = knop_blauw.value()
    waarde_twee = knop_rood.value()
    print(teller, waarde, waarde_twee)
    teller += 1
    if waarde:
        if not pin:
            for id in PINNEN:
                pin.append(Pin(id, Pin.OUT) )
        
        pin[led_index].on()
        sleep(0.2)
        pin[led_index].off()
        sleep(0.2)
        
        led_index = (led_index + 1) % len(pin)