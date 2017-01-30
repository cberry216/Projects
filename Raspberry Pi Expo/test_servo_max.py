import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.OUT)

p = GPIO.PWM(12,100)

p.start(15)

try:
    while True:
        p.ChangeDutyCycle(6.5)
        time.sleep(1)
        p.ChangeDutyCycle(23.5)
        time.sleep(1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
    
