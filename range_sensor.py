import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print("Distance measurement in progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("Waiting for sensor")
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == 0:
    pulse_start = time.time()

while GPIO.input(ECHO) == 1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print("Distance:",distance,"cm")

GPIO.cleanup()

WALL_DISTANCE = 0 # need to test for this values
error = 0 # need to test for this values

# Now check if any object is closer than the wall

if abs(WALL_DISTANCE - distance) > error:
    # make thermal camera take a picture

