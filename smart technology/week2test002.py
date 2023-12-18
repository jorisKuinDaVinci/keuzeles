import machine
import time

SLEEP  = 2
#INTERNAL_LED = 25  # pico-H
INTERNAL_LED = "LED" # pico-W

led = machine.Pin(INTERNAL_LED

for led in pin:    
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)