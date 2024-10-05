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
    turn = min(1600,max(800,1200 -error*kP))
    return turn
pi = pigpio.pi()
pi.set_mode(18,pigpio.OUTPUT)
pi.set_mode(13,pigpio.OUTPUT)
i2c = busio.I2C(board.SCL, board.SDA)
ser = serial.Serial('/dev/ttyACM0', 9600)
sensor = adafruit_bno055.BNO055_I2C(i2c)
heading = 0.0
roll = 0.0
pitch =0.0
dis = 0.0
value = 0
count = 0
increment    = False
logic = False
flag = True
time.sleep(3)
def R_journey(heading,distanceRight,value, logic, flag, increment, count,init):
    if init:
        value = 0
        count = 0
        increment    = False
        logic = False
        flag = True
        init = False
        print("Initializeeeeeeeeeed")
    #try:
#     img = picam2.capture_array()
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img = cv2.flip(img,-1)
#     img[0:240, 50:640,:] = 255
#     img[0:80, 0:50,:] = 255
#     img,x = color_detect(img, (0,0,0) , (255,50,50))
#     cv2.imshow("frame",img)

#         dis1,dis,dis3 = map(float, data.split(','))
#     except:
#         dis1 = dis = dis3 = 0
    #except:
   # heading = 0
    #dis = 0.0
#         heading = 0
    if((distanceRight)>=120 or logic):
        if(flag):
            value +=90
            if value == 360:
                value = 0
                increment = True
            flag = False
            
        if((heading) not in range(value-5,value+60)):
            print("turning", heading, value, distanceRight)
            if heading >=350 and value == 90:
                pi.set_servo_pulsewidth(18,1500)
            elif value ==  0 and heading>=260:
                pi.set_servo_pulsewidth(18,max(950,min(1550,1200 + (value-heading+360)*18)))
                print("Condition b")
            else:
                pi.set_servo_pulsewidth(18,max(950,min(1550,1200 + (value-heading)*18)))
            pi.set_servo_pulsewidth(13,1570)
            logic = True
        else:
             pi.set_servo_pulsewidth(18,1200)
             pi.set_servo_pulsewidth(13,1570)
#              print("Exited turnloop")
             logic = False
             time.sleep(0.08)
    else:
        flag = True
        if increment:
            count = count + 1
            increment = False
        print(heading,distanceRight, value)
        pi.set_servo_pulsewidth(18,pid(value,heading,20))        
        pi.set_servo_pulsewidth(13,1570)
    return value,logic,flag,increment,count
    



