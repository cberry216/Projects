import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18

print 'Distance Measurement in Progress'

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG,False)
print 'Waiting For Sensor to Settle'
time.sleep(1)

#pulse
GPIO.output(TRIG,True)
time.sleep(.00001)
GPIO.output(TRIG,False)

while GPIO.input(ECHO) == False:
    pulse_start = time.time()
while GPIO.input(ECHO) == True:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance,2)

print 'Distance: ' + distance + ' cm'

GPIO.cleanup()
