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


def stepper_f(delay,steps):
    for i in range(steps):
        Step(1,1,0,0)
        time.sleep(delay)
        Step(0,1,1,0)
        time.sleep(delay)
        Step(0,0,1,1)
        time.sleep(delay)
        Step(1,0,0,1)
        time.sleep(delay)

def stepper_b(delay,steps):
    for i in range(steps):
        Step(1,1,0,0)
        time.sleep(delay)
        Step(1,0,0,1)
        time.sleep(delay)
        Step(0,0,1,1)
        time.sleep(delay)
        Step(0,1,1,0)
        time.sleep(delay)

try:
    while True:
        steps = int(raw_input('Number of steps: '))
        delay = int(raw_input('Delay in ms: '))
        stepper_f(delay/1000.0, steps)
        stepper_b(delay/1000.0, steps)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
