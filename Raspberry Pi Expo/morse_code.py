import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)


phrase = raw_input("Enter a phrase to be translated to morse code:\n").lower()

dot = "."
dash = "-"
brk = "/"
pause = "_"

alpha = [dot+dash,dash+dot+dot+dot,dash+dot+dash+dot,dash+dot+dot,dot,dot+dot+dash+dot,dash+dash+dot,dot+dot+dot+dot,dot+dot,dot+dash+dash+dash,dash+dot+dash,dot+dash+dot+dot,
         dash+dash,dash+dot,dash+dash+dash,dot+dash+dash+dot,dash+dash+dot+dash,dot+dash+dot,dot+dot+dot,dash,dot+dot+dash,dot+dot+dot+dash,dot+dash+dash,dash+dot+dot+dash,
         dash+dot+dash+dash,dash+dash+dot+dot,brk]

new_phrase = ""

for i in phrase:
        if ord(i) == 32:
                new_phrase += pause
        else:
                new_phrase += alpha[ord(i) - 97] + brk

print new_phrase

for i in new_phrase:
        if i == dot:
                GPIO.output(7,True)
                time.sleep(.2)
                GPIO.output(7,False)
		time.sleep(.2)
        if i == dash:
                GPIO.output(7,True)
                time.sleep(.4)
                GPIO.output(7,False)
		time.sleep(.2)
        if i == brk:
                time.sleep(.5)
                GPIO.output(7,False)
        if i == pause:
                time.sleep(.5)
                GPIO.output(7,False)

print 'Done'

GPIO.cleanup()


