import RPi.GPIO as GPIO
import time
from ultrasonic_sensor import UltrasonicSensor
from event import Event

def setup(sensor):
    print("Setting up sensor: " + sensor.name)
    GPIO.setup(sensor.trigger, GPIO.OUT) 
    GPIO.setup(sensor.echo, GPIO.IN)
    GPIO.output(sensor.trigger, False)

def sendPulse(sensor):
    time.sleep(0.5)
    GPIO.output(sensor.trigger, True)
    time.sleep(0.00001)
    GPIO.output(sensor.trigger, False)
    print("Pulse sent from sensor: " + sensor.name)

def calcDistance(sensor):
    SPEED_OF_SOUND = 17150
    total_time = sensor.pulse_end - sensor.pulse_start
    distance = SPEED_OF_SOUND * total_time
    sensor.distance = distance
    print(sensor.distance)

def readDistance(sensor):
    sendPulse(sensor)
    print("Reading sensor: " + sensor.name)
    while GPIO.input(sensor.echo) == 0:
        sensor.pulse_start = time.time()
    while GPIO.input(sensor.echo) == 1:
        sensor.pulse_end = time.time()
    calcDistance(sensor)

def main():
    
    # Pins where the sensors are connected to the PI
    TRIG_1 = 25
    ECHO_1 = 12
    TRIG_2 = 23
    ECHO_2 = 24
    
    
    WALL_DISTANCE = 25
    TOLERANCE = 5

    # Initialize sensors
    enter_sensor = UltrasonicSensor("enter", TRIG_1, ECHO_1)
    exit_sensor = UltrasonicSensor("exit", TRIG_2, ECHO_2)
    
    print(enter_sensor)
    print(exit_sensor)

    # Initalize GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Setting up sensors
    setup(enter_sensor)
    setup(exit_sensor)
    i=0
    while i<100:
        readDistance(enter_sensor)
        time.sleep(0.1)
        readDistance(exit_sensor)

        if(enter_sensor.distance < (WALL_DISTANCE - TOLERANCE)):
            while(enter_sensor.distance < (WALL_DISTANCE - TOLERANCE)):
                print("Waiting for person to leave enter sensor")
                time.sleep(0.1)
                readDistance(enter_sensor)

            # take 3 pictures
            print("Person entering")

            start_time = time.time()
            while True:
                print("Waiting for person to reach exit sensor")
                if time.time() - start_time > 10:
                    break
                time.sleep(0.1)
                readDistance(exit_sensor)
                if(exit_sensor.distance < (WALL_DISTANCE - TOLERANCE)):
                    
                    while(exit_sensor.distance < (WALL_DISTANCE - TOLERANCE)):
                        print("Waiting for person to leave exit sensor")
                        time.sleep(0.1)
                        readDistance(exit_sensor)
                    
                    break
        
        elif(exit_sensor.distance < (WALL_DISTANCE - TOLERANCE)):
            while(exit_sensor.distance < (WALL_DISTANCE - TOLERANCE)):
                print("Waiting for person to leave exit sensor 1")
                time.sleep(0.1)
                readDistance(exit_sensor)

            # take 3 pictures
            print("Person exiting")

            start_time = time.time()
            while True:
                print("Waiting for person to reach enter sensor 1")
                if time.time() - start_time > 10:
                    break
                time.sleep(0.1)
                readDistance(enter_sensor)
                if(enter_sensor.distance < (WALL_DISTANCE - TOLERANCE)):
                    while(enter_sensor.distance < (WALL_DISTANCE - TOLERANCE)):
                        print("Waiting for person to leave enter sensor 1")
                        time.sleep(0.1)
                        readDistance(enter_sensor)
                    
                    break

        i+=1
        
    GPIO.cleanup()
        
if __name__ == "__main__":
    main()




