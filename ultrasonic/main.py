import RPi.GPIO as GPIO
import time
from ultrasonic_sensor import UltrasonicSensor
from event import Event

def main():
    
    # Pins where the sensors are connected to the PI
    TRIG_1 = 25
    ECHO_1 = 12
    TRIG_2 = 23
    ECHO_2 = 24
    
    
    WALL_DISTANCE = 50
    TOLERANCE = 15

    # Initialize sensors
    enter_sensor = UltrasonicSensor("enter", TRIG_1, ECHO_1)
    exit_sensor = UltrasonicSensor("exit", TRIG_2, ECHO_2)
    
    print(enter_sensor)
    print(exit_sensor)

    # Initalize GPIO
    gpio = GPIO()
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)

    # Setting up sensors
    enter_sensor.setup(gpio)
    exit_sensor.setup(gpio)

    while True:
        enter_sensor.read_distance()
        time.sleep(0.5)
        exit_sensor.read_distance()

        
            






if __name__ == "__main__":
    main()




