import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16,GPIO.OUT)

try:
    while True:
        GPIO.output(16,True)
except KeyboardInterrupt:
    pass

GPIO.cleanup()


        
