from machine import Pin
from time import sleep

PIN=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)

pin=[]

knop_zwart = Pin(17, Pin.IN)

knop_rood = Pin(16, Pin.IN)

for id in PIN:
    pin.append(Pin(id, Pin.OUT))
    
index = 7
knopIngedrukt = knop_zwart.value() == 1
if knopIngedrukt == False:
    for led in pin:
          led.on()
          sleep(0.2)
          
          while not knopIngedrukt:
              knopIngedrukt = knop_zwart.value() == 1
              sleep(0.2)
              
          led.off()
          sleep(0.2)    
          index -= 1   
else:
    knopIngedrukt == True
    for led in pin:
          led.on()
          sleep(0.2)
          
          while knopIngedrukt:
              knopIngedrukt = knop_zwart.value() == 1
              sleep(0.2)
              
          led.off()
          sleep(0.2)    
          index += 1
#leds[index].on()
#leds[index].off()