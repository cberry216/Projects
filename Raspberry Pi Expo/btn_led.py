import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.OUT)

pwm = GPIO.PWM(12, 50)
pwm.start(0)

dc_count = 0

try:
        while True:
                in_state = GPIO.input(18)
                if in_state == False:
                        dc_count += 1
                        if dc_count % 5 == 1:
                                pwm.ChangeDutyCycle(25)
                                time.sleep(0.2)
                        elif dc_count % 5 == 2:
                                pwm.ChangeDutyCycle(50)
                                time.sleep(0.2)
                        elif dc_count % 5 == 3:
                                pwm.ChangeDutyCycle(75)
                                time.sleep(0.2)
                        elif dc_count % 5 == 4:
                                pwm.ChangeDutyCycle(100)
                                time.sleep(0.2)
                        else:
                                pwm.ChangeDutyCycle(0)
                                time.sleep(0.2)
except KeyboardInterrupt:
        pass

pwm.stop()
GPIO.cleanup()

