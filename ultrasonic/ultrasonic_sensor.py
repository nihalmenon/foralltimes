

class UltrasonicSensor:

    def __init__(self, name, trig, echo):
        self.name = name
        self.trigger = trig
        self.echo = echo
        self.pulse_start = -1
        self.pulse_end = -1
        self.distance = -1
    
    def __str__(self):
        return f"Trigger: {self.trigger}, Echo: {self.echo}, Pulse start: {self.pulse_start}, Pulse end: {self.pulse_end}, Distance: {self.distance}"

    
    


        
    
