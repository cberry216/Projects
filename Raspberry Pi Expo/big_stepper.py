import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

en = 37
ms2 = 35
ms1 = 33
step = 31
dirc = 29

GPIO.setup(en,GPIO.OUT)
GPIO.setup(ms2,GPIO.OUT)
GPIO.setup(ms1,GPIO.OUT)
GPIO.setup(step,GPIO.OUT)
GPIO.setup(dirc,GPIO.OUT)

GPIO.output(en,False)
GPIO.output(ms1,True)
GPIO.output(ms2,True)

def Step(delay):
    GPIO.output(31,True)
    time.sleep(delay)
    GPIO.output(31,False)
    time.sleep(delay)

def stepper_f(delay,steps):
    GPIO.output(29,False)
    for i in range(steps):
        Step(delay)

def stepper_b(delay,steps):
    GPIO.output(29,True)
    for i in range(steps):
        Step(delay)

try:
    while True:
        steps = int(raw_input("Enter number of steps: "))
        delay = float(raw_input("Enter delay of steps: "))
        forward = raw_input("Forward[Y] or Backward[N]: ").lower()
        if forward == 'y':
            stepper_f(delay,steps)
        else:
            stepper_b(delay,steps)
except KeyboardInterrupt:
    GPIO.cleanup()

