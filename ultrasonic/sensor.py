import RPi.GPIO as GPIO
import time

class UltrasonicSensor:

    def __init__(self, name, trig, echo):
        self.name = name
        self.trigger = trig
        self.echo = echo
        self.pulse_start = -1
        self.pulse_end = -1
        self.distance = -1
    
    def __str__(self):
        return f"Trigger: {self.trigger}, Echo: {self.echo}, Pulse start: {self.pulse_start}, Pulse end: {self.pulse_end}, Distance: {self.curr_distance}"

    def setup(self, gpio):
        print("Setting up sensor: " + self.name)
        gpio.setup(self.trigger, gpio.OUT) 
        gpio.setup(self.echo, gpio.IN)
        gpio.output(self.trigger, False)

    def sendPulse(self, gpio):
        time.sleep(1)
        gpio.output(self.trigger, True)
        time.sleep(0.00001)
        gpio.output(self.trigger, False)
        print("Pulse sent from sensor: " + self.name)
    
    def calcDistance(self):
        SPEED_OF_SOUND = 17150
        total_time = self.pulse_end - self.pulse_start
        distance = SPEED_OF_SOUND * total_time
        self.distance = distance

    def read_distance(self, gpio):
        self.send_pulse()
        print("Reading sensor: " + self.name)
        while gpio.input(self.echo) == 0:
            self.pulse_start = time.time()
        while gpio.input(self.echo) == 1:
            self.pulse_end = time.time()
        self.calcDistance()
    


        
    
