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

def deg_to_steps(deg):
    return int(round(deg*40/9))

try:
    while True:
        ans = raw_input('Enter one input at a time[0] or a sequence[1]: ')
        if ans == '0':
            deg_str = '-1'
            while len(deg_str) > 0:
                deg_str = raw_input('Enter degrees to turn (negative for clockwise): ')
                if len(deg_str) > 0:
                    deg = float(deg_str)
                    steps = deg_to_steps(deg)
                    if steps < 0:
                        stepper_f(.0005,steps*-1)
                    else:
                        stepper_b(.0005,steps)
        else:
            sequence = []
            seq_val = '-1'
            while len(seq_val) > 0:
                seq_val = raw_input('Enter value to be added to sequence (Hit Enter twice to confirm sequence: ')
                if len(seq_val) > 0:
                    val = float(seq_val)
                    sequence.append(val)
                    print sequence
            step_seq = []
            for i in sequence:
                step_seq.append(deg_to_steps(i))
            for i in step_seq:
                if i < 0:
                    stepper_f(.0005,i*-1)
                else:
                    stepper_b(.0005,i)
                time.sleep(.01)
                
except KeyboardInterrupt:
    GPIO.cleanup()
        
