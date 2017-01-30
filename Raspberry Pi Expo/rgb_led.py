import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pins = [29,31,33]

GPIO.setup(pins, GPIO.OUT)

GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        rgb_count = 0
        input_state = GPIO.input(37)
        if input_state == False:
            rgb_count += 1
            GPIO.output(pins, False)
            if rgb_count % 8 == 1:
                GPIO.output(29, True)
            elif rgb_count % 8 == 2:
                GPIO.output(31, True)
            elif rgb_count % 8 == 3:
                GPIO.output(33, True)
            elif rgb_count % 8 == 4:
                GPIO.output(29, True)
                GPIO.output(31, True)
            elif rgb_count % 8 == 5:
                GPIO.output(29, True)
                GPIO.output(33, True)
            elif rgb_count % 8 == 6:
                GPIO.output(31, True)
                GPIO.output(33, True)
            elif rgb_count % 8 == 7:
                GPIO.output(29, True)
                GPIO.output(31, True)
                GPIO.output(33, True)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
            
        
