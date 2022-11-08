import RPi.GPIO as GPIO
import time

try:
      GPIO.setmode(GPIO.BOARD)

      PIN_TRIGGER = 7
      PIN_ECHO = 11

      PIN_TRIGGER2 = 5
      PIN_ECHO2 = 9

      passedFirst = 0
      passedSecond = 0
      leaving = False 
      entering = True
      left = 0
      enter =0

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)

      GPIO.setup(PIN_TRIGGER2, GPIO.OUT)
      GPIO.setup(PIN_ECHO2, GPIO.IN)

      
      GPIO.output(PIN_TRIGGER2, GPIO.LOW)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      print ("Waiting for sensor to settle")

      time.sleep(2)

      print ("Calculating distance")

      GPIO.output(PIN_TRIGGER, GPIO.HIGH)
      GPIO.output(PIN_TRIGGER2, GPIO.HIGH)
      
      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)
      GPIO.output(PIN_TRIGGER2, GPIO.LOW)
     
      wall=0
      while True:
        while GPIO.input(PIN_ECHO)==0:
                pulse_start_time = time.time()
        
        while GPIO.input(PIN_ECHO2)==0:
                pulse_start_time2 = time.time()
        
        while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()

        while GPIO.input(PIN_ECHO2)==1:
                pulse_end_time2 = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance1 = round(pulse_duration * 17150, 2)
        print ("Distance:",distance1,"cm")
        pulse_duration2 = pulse_end_time2 - pulse_start_time2
        distance2 = round(pulse_duration2 * 17150, 2)
        print ("Distance:",distance2,"cm")

        if (wall > distance2):
            passedSecond = 1
        if (wall > distance1):
            passedFirst =1

        if (wall > distance1 or wall > distance2):
            
            if (passedFirst ):
                # leaving 
                leaving = True; 
                left += 1
                



finally:
      GPIO.cleanup()

