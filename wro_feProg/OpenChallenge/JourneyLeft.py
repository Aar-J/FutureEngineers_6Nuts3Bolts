import time
import board
import busio
import adafruit_bno055
import sys
import serial
sys.path.append('/usr/lib/python3/dist-packages')
import pigpio
from picamera2 import Picamera2, Preview
import cv2

def pid(y, heading,kP):
    if(y<360-y):
        y = y
    elif (y == 360-y):
        y=180
    else:
        y = -360+y
    if(heading<360-heading):
        heading = heading
    elif (heading == 360-heading):
        heading=180
    else:
        heading = -360+heading
    if heading<0 and y<0:
        error = heading-y
    elif heading<0 and y>0:
        error = y+heading
    else:
        error = heading - y
    turn = min(2000,max(1000,1500 -error*kP))
    return turn
pi = pigpio.pi()
pi.set_mode(18,pigpio.OUTPUT)
pi.set_mode(13,pigpio.OUTPUT)
i2c = busio.I2C(board.SCL, board.SDA)
ser = serial.Serial('/dev/ttyUSB0', 9600)
sensor = adafruit_bno055.BNO055_I2C(i2c)
heading = 0.0
roll = 0.0
pitch =0.0
dis = 0.0
value = 360
count = 0
increment    = False
logic = False
flag = True
time.sleep(3)
def L_journey(heading,dis,value, logic, flag, increment, count,init):
    if init:
        value = 360
        count = 0
        increment    = False
        logic = False
        flag = True
        init = False
        print("Initializeeeeeeeeeed")

    if((dis)>=120 or logic):
        if(flag):
            value -=90
            if value == 0:
                value = 360
                increment = True
            flag = False
            
        if((heading) not in range(value-60,value+5)):
            print("turning", heading, value, dis)
            if heading <=10 and value == 270:
                pi.set_servo_pulsewidth(18,1100)
                pi.set_servo_pulsewidth(13,1560)
            elif value ==  360 and heading<=100:
                pi.set_servo_pulsewidth(18,max(1100,min(1900,1500 + ((value-360)-heading)*18)))
                pi.set_servo_pulsewidth(13,1560)
                print("Condition b")
            else:
                pi.set_servo_pulsewidth(18,max(1100,min(1900,1500 + (value-heading)*18)))
                pi.set_servo_pulsewidth(13,1560)
            logic = True
        else:
             pi.set_servo_pulsewidth(18,1600)
             pi.set_servo_pulsewidth(13,1560)
#              print("Exited turnloop")
             logic = False
             time.sleep(0.3)
    else:
        flag = True
        if increment:
            count = count + 1
            increment = False
        print(heading,dis, value)
        pi.set_servo_pulsewidth(18,pid(value,heading,20))        
        pi.set_servo_pulsewidth(13,1560)
    return value,logic,flag,increment,count
    
def move(heading, value):
    pi.set_servo_pulsewidth(18,pid(value,heading,20))        
    pi.set_servo_pulsewidth(13,1550)

