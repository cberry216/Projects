import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

GPIO.output(16,True)
GPIO.output(21,False)

def getReading(pin):
    
    reading = 0
    
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)
    time.sleep(.1)

    GPIO.setup(pin,GPIO.IN)
    while(GPIO.input(pin) == False):
        reading += 1
    return reading

try:
    while True:
        read = getReading(23)
        print read
        if read > 12000:
            GPIO.output(21,True)
        else:
            GPIO.output(21,False)
        time.sleep(.25)
except KeyboardInterrupt:
    GPIO.output(16,False)
    
GPIO.cleanup()
