from machine import Pin
from utime import sleep
from utime import ticks_us

PINNEN = (0,2,7,12,20,28,27)
pin = []
knop = Pin(20, Pin.IN)


TRIG_PIN = 28  # Ultrasonic sensor trigger
ECHO_PIN = 27  # Ultrasonic sensor echo
LED1_PIN = 0  # LED 1
LED2_PIN = 5  # LED 2
LED3_PIN = 7 # LED 3
LED4_PIN = 12 # LED 4


led1 = machine.Pin(LED1_PIN, machine.Pin.OUT)
led2 = machine.Pin(LED2_PIN, machine.Pin.OUT)
led3 = machine.Pin(LED3_PIN, machine.Pin.OUT)
led4 = machine.Pin(LED4_PIN, machine.Pin.OUT)
trig = machine.Pin(TRIG_PIN, machine.Pin.OUT)
echo = machine.Pin(ECHO_PIN, machine.Pin.IN)


for id in PINNEN:
    pin.append(Pin(id, Pin.OUT))


def meet_afstand():
    trig.low()
    sleep(2)
    trig.high()
    sleep(5)
    trig.low()
    
    while echo.value() == 0:
        signaloff = ticks_us()
    
    while echo.value() == 1:
        signalon = ticks_us()
    
    timepassed = signalon - signaloff
    afstand = (timepassed * 0.0343) / 2
    
    return afstand  

while True:
    if knop.value() == 1:
        afstand = meet_afstand()
    
        print("afstand: {} cm".format(afstand))
    
    
        if afstand <= 30:
            for led in pin:
                led2.off()
                led1.on()
        if afstand > 30:
            for led in pin:
                led2.on()
        if afstand <= 20:
            for led in pin:
                led2.off()
                led3.on() 
        if afstand <= 10:
            for led in pin:
                led2.off()
                led4.on()        