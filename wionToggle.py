## Import GPIO library
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

## Use BCM (more later) pin numbering
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, True)
time.sleep(1)
GPIO.output(17, False)
