import RPi.GPIO as GPIO
import time
 
TRIG = 3 
ECHO = 5

def initDistanceGPIO():
 
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

def checkdist():
    GPIO.output(TRIG, 0)
    time.sleep(0.01)
 
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)
    start = time.time()
 
    while GPIO.input(ECHO) == 0:
      start = time.time()
 
    while GPIO.input(ECHO) == 1:
      stop = time.time()
 
    distance = (stop - start) * 34000 / 2 
    print 'Distance: %0.2f cm' %distance
 

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    initDistanceGPIO()
    try:
        while True:
            checkdist()
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()

