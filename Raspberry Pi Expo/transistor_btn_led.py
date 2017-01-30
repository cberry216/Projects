import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)

state = 1

try:
    while True:
        input_state = GPIO.input(16)
        if(input_state == False):
            if(state % 2 == 1):
                GPIO.output(11,True)
                state += 1
            else:
                GPIO.output(11,False)
                state += 1
except KeyboardInterrupt:
    pass

GPIO.cleanup()
