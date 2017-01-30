import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

step_pin = [11,12,13,15]
btn = 32

GPIO.setup(step_pin,GPIO.OUT)
GPIO.setup(btn,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def Step(s1,s2,s3,s4):
    GPIO.output(step_pin[0],s1)
    GPIO.output(step_pin[1],s2)
    GPIO.output(step_pin[2],s3)
    GPIO.output(step_pin[3],s4)

step = 0

try:
    while True:
        btn_press = GPIO.input(btn)
        if btn_press == 0:
            if step == 0:
                Step(1,0,0,1)
                step+=1
            elif step == 1:
                Step(0,1,0,1)
                step+=1
            elif step == 2:
                Step(0,1,1,0)
                step+=1
            elif step == 3:
                Step(1,0,1,0)
                step = 0
            time.sleep(.25)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
