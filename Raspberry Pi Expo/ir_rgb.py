import RPi.GPIO as GPIO
import time
import lirc
import os

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)

GPIO.setup(18,GPIO.OUT)

red = GPIO.PWM(40,60)
grn = GPIO.PWM(38,60)
blu = GPIO.PWM(35,60)

rdc = 0
gdc = 0
bdc = 0

cur_rdc = 0
cur_gdc = 0
cur_bdc = 0

red.start(rdc)
grn.start(gdc)
blu.start(bdc)

last_btn = -1

power = True
GPIO.output(18,power)

ir_id = lirc.init("ir_rgb", blocking=False)

def dim():
    global rdc, gdc, bdc
    rdc = rdc * .9
    gdc = gdc * .9
    bdc = bdc * .9
    if rdc < 1 and gdc < 1 and bdc < 1:
        rdc = 0
        gdc = 0
        bdc = 0
    red.ChangeDutyCycle(rdc)
    grn.ChangeDutyCycle(gdc)
    blu.ChangeDutyCycle(bdc)

def bright(max_rdc, max_gdc, max_bdc):
    global rdc, gdc, bdc
    rdc = rdc * 1.1
    gdc = gdc * 1.1
    bdc = bdc * 1.1
    if rdc == 0:
        if max_rdc > 0:
            rdc = 1
    if rdc > max_rdc:
        rdc = max_rdc
    if gdc == 0:
        if max_gdc > 0:
            gdc = 1
    if gdc > max_gdc:
        gdc = max_gdc
    if bdc == 0:
        if max_bdc > 0:
            bdc = 1
    if bdc > max_bdc:
        bdc = max_bdc
    red.ChangeDutyCycle(rdc)
    grn.ChangeDutyCycle(gdc)
    blu.ChangeDutyCycle(bdc)

def skip():
    #os.system('irsend SEND_ONCE /etc/lirc/IRColorController KEY_G')
    global last_btn
    if last_btn == 1:
        os.system('irsend SEND_ONCE /etc/lirc/IRColorController KEY_G')
    elif last_btn == 2:
        os.system('irsend SEND_ONCE /etc/lirc/IRColorController KEY_B')
    elif last_btn == 3:
        os.system('irsend SEND_ONCE /etc/lirc/IRColorController KEY_W')
    elif last_btn == 4:
        os.system('irsend SEND_ONCE /etc/lirc/IRColorController KEY_5')
    elif last_btn <= 19:
        os.system('irsend SEND_ONCE /etc/lirc/IRColorController KEY_%s' % str(last_btn+1))
    else:
        os.system('irsend SEND_ONCE /etc/lirc/IRColorController KEY_R')
    

while True:
    code_ir = lirc.nextcode()
    if code_ir:
        if code_ir[0] =='r':
            rdc = 100
            gdc = 0
            bdc = 0
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 1
        if code_ir[0] =='g':
            rdc = 0
            gdc = 100
            bdc = 0
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 2
        if code_ir[0] =='b':
            rdc = 0
            gdc = 0
            bdc = 100
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 3
        if code_ir[0] =='w':
            rdc = 100
            gdc = 100
            bdc = 100
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 4
        if code_ir[0] =='5':
            rdc = 92.55
            gdc = 41.96
            bdc = 0
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 5
        if code_ir[0] =='6':
            rdc = 0
            gdc = 78.82
            bdc = 33.33
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 6
        if code_ir[0] =='7':
            rdc = 0
            gdc = 57.25
            bdc = 100
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 7
        if code_ir[0] =='8':
            rdc = 100
            gdc = 74.51
            bdc = 74.51
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 8
        if code_ir[0] =='9':
            rdc = 100
            gdc = 31.37
            bdc = 31.37
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 9
        if code_ir[0] =='10':
            rdc = 27.45
            gdc = 83.53
            bdc = 100
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 10
        if code_ir[0] =='11':
            rdc = 13.33
            gdc = 0
            bdc = 100
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 11
        if code_ir[0] =='12':
            rdc = 100
            gdc = 66.66
            bdc = 66.66
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 12
        if code_ir[0] =='13':
            rdc = 100
            gdc = 70.98
            bdc = 54.90
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 13
        if code_ir[0] =='14':
            rdc = 0
            gdc = 87.45
            bdc = 100
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 14
        if code_ir[0] =='15':
            rdc = 65.49
            gdc = 0
            bdc = 16.47
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 15
        if code_ir[0] =='16':
            rdc = 73.73
            gdc = 96.47
            bdc = 100
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 16
        if code_ir[0] =='17':
            rdc = 100
            gdc = 100
            bdc = 0
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 17
        if code_ir[0] =='18':
            rdc = 0
            gdc = 34.12
            bdc = 54.51
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 18
        if code_ir[0] =='19':
            rdc = 100
            gdc = 0
            bdc = 65.49
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 19
        if code_ir[0] =='20':
            rdc = 66.66
            gdc = 92.55
            bdc = 100
            cur_rdc = rdc
            cur_gdc = gdc
            cur_bdc = bdc
            red.ChangeDutyCycle(rdc)
            grn.ChangeDutyCycle(gdc)
            blu.ChangeDutyCycle(bdc)
            last_btn = 20
        if code_ir[0] == 'power':
            power = not(power)
            GPIO.output(18,power)
        if code_ir[0] == 'light_down':
            dim()
        if code_ir[0] == 'light_up':
            bright(cur_rdc,cur_gdc,cur_bdc)
        if code_ir[0] == 'skip':
            skip()
        if code_ir[0] == 'r_up':
            rdc += 5
            if rdc > 100.0:
                rdc = 100
            red.ChangeDutyCycle(rdc)
        if code_ir[0] == 'g_up':
            gdc += 5
            if gdc > 100.0:
                gdc = 100
            grn.ChangeDutyCycle(gdc)
        if code_ir[0] == 'b_up':
            bdc += 5
            if bdc > 100.0:
                bdc = 100
            blu.ChangeDutyCycle(bdc)
        if code_ir[0] == 'r_down':
            rdc -= 5
            if rdc < 0:
                rdc = 0
            red.ChangeDutyCycle(rdc)
        if code_ir[0] == 'g_down':
            gdc -= 5
            if gdc < 0:
                gdc = 0
            grn.ChangeDutyCycle(gdc)
        if code_ir[0] == 'b_down':
            bdc -= 5
            if bdc < 0:
                bdc = 0
            blu.ChangeDutyCycle(bdc)

GPIO.cleanup()
