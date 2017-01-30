import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
"""
    LED 1 -> 11
    LED 2 -> 13
    LED 3 -> 15
    LED 4 -> 16
    LED 5 -> 18
    LED 6 -> 22
    LED 7 -> 29
    LED 8 -> 31

    BTN -> 31
"""

GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pins = [11,13,15,16,18,22,29,31]

try:
    while True:
	GPIO.output(pins, False)
        input_state = GPIO.input(36)
        if input_state == False:
            for i in range(0, len(pins) + 3):
		if i < len(pins):
                	GPIO.output(pins[i],True)
                if(i >= 3):
                    GPIO.output(pins[i-3], False)
                time.sleep(.1)

except KeyboardInterrupt:
        print 'Done'

GPIO.cleanup()
