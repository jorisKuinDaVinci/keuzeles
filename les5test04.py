from machine import Pin
from time import sleep

PIN = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

pin = []

knop_zwart = Pin(28, Pin.IN)

for id in PIN:
    pin.append(Pin(id, Pin.OUT))
    
teller = 0
while True:
      for led in pin:
          led.on()
          sleep(0.2)
          
          knopIngedrukt = False
          while not knopIngedrukt:
              knopIngedrukt = knop_zwart.value() == 1
              sleep(0.2)
              
          led.off()
          sleep(0.2)
          teller += 1
          
          
# led_1 = Pin(0, Pin.OUT)          