import RPi.GPIO as GPIO
import time
import lirc

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)

p = GPIO.PWM(40,100)

p.start(15)

ir_id = lirc.init("ir_servo", blocking = False)

try:
    while True:
        code_ir = lirc.nextcode()
        if code_ir[0] == "pos_0":
            p.ChangeDutyCycle(6.5)
        elif code_ir[0] == "pos_1":
            p.ChangeDutyCycle(15)
        elif code_ir[0] == "pos_2":
            p.ChangeDutyCycle(23.25)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
            
