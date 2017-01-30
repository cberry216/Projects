import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(37,GPIO.OUT)

try:
    while True:
        GPIO.output(37,True)
        time.sleep(.5)
        GPIO.output(37,False)
        time.sleep(.5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
