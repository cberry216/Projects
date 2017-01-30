import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

GPIO.output(7,True)
GPIO.output(11,False)
time.sleep(1)
GPIO.output(7,False)
GPIO.output(11, True)
time.sleep(1)
GPIO.output(7,True)
GPIO.output(11,False)
time.sleep(1)
GPIO.output(7,False)
GPIO.output(11,True)
time.sleep(1)

print "Done"

GPIO.cleanup()
