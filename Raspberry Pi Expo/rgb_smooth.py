import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pins = [21,20,12]

GPIO.setup(pins, GPIO.OUT)

GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)

p1_dc = 100
p2_dc = 0
p3_dc = 0

p1 = GPIO.PWM(21,50)
p2 = GPIO.PWM(20,50)
p3 = GPIO.PWM(12,50)

p1.start(p1_dc)
p2.start(p2_dc)
p3.start(p3_dc)

try:
    while True:
        input_state = GPIO.input(37)
        if input_state == False:
            while p2_dc < 100:
                p2_dc += .1
                p2.ChangeDutyCycle(p2_dc)
                time.sleep(.05)
            while p1_dc > 0:
                p1_dc -= .1
                p1.ChangeDutyCycle(p1_dc)
                time.sleep(.05)
            while p3_dc < 100:
                p3_dc += .1
                p3.ChangeDutyCycle(p3_dc)
                time.sleep(.05)
            while p2_dc > 0:
                p2_dc -= .1
                p2.ChangeDutyCycle(p2_dc)
                time.sleep(.05)
            while p1_dc < 100:
                p1_dc += .1
                p1.ChangeDutyCycle(p1_dc)
                time.sleep(.05)
            while p3_dc > 0:
                p3_dc -= .1
                p3.ChangeDutyCycle(p2_dc)
                time.sleep(.05)
except KeyboardInterrupt:
    print 'Done'

p1.stop()
p2.stop()
p3.stop()

GPIO.cleanup()

