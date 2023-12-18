import machine
from time import sleep

class Servo:
    def __init__(self, MIN_DUTY=300000, MAX_DUTY=2300000, pin=0, freq=50):