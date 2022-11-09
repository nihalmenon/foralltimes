import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG_1 = 12
ECHO_1 = 11
TRIG_2 = 9
ECHO_2 = 8

direction = -1 # 0 is out and 1 is in

print("Distance measurement in progress")

GPIO.setup(TRIG_1, GPIO.OUT)
GPIO.setup(ECHO_1, GPIO.IN)
GPIO.setup(TRIG_2, GPIO.OUT)
GPIO.setup(ECHO_2, GPIO.IN)

GPIO.output(TRIG_1, False)
print("Waiting for sensor 1")
time.sleep(2)

GPIO.output(TRIG_1, True)
time.sleep(.00001)
GPIO.output(TRIG_1, False)

while GPIO.input(ECHO_1) == 0:
    pulse_start_1 = time.time()

while GPIO.input(ECHO_1) == 1:
    pulse_end_1 = time.time()


pulse_duration_1 = pulse_end_1 - pulse_start_1

distance_1 = pulse_duration_1 * 17150
distance_1 = round(distance_1, 2)

GPIO.output(TRIG_2, False)
print("Waiting for sensor 2")
time.sleep(2)

while GPIO.input(ECHO_2) == 0:
    pulse_start_2 = time.time()

while GPIO.input(ECHO_2) == 1:
    pulse_end_2 = time.time()

pulse_duration_2 = pulse_end_2 - pulse_start_2

distance_2 = pulse_duration_2 * 17150
distance_2 = round(distance_2, 2)


print("Distance 1:",distance_1,"cm\n")
print("Distance 2:",distance_2,"cm\n")

GPIO.cleanup()

WALL_DISTANCE = 0 # need to test for this values
error = 0 # need to test for this values
time_error = 0

# Now check if any object is closer than the wall

if (abs(WALL_DISTANCE - distance_1) > error or abs(WALL_DISTANCE - distance_2) > error):
    if (pulse_end_2 - pulse_end_1) > time_error:
        direction = 1
    elif (pulse_end_1 - pulse_end_2) > time_error:
        direction = 0
    
    # take thermal picture

print(direction)
