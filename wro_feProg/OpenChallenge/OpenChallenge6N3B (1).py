import time
import board
import busio
import adafruit_bno055
import sys
import serial
sys.path.append('/usr/lib/python3/dist-packages')
BUTTON_PIN=17
import pigpio
from picamera2 import Picamera2, Preview
import cv2

import JourneyLeft as l
import JourneyRight as r

pi = pigpio.pi()
pi.set_mode(18,pigpio.OUTPUT)
pi.set_mode(13,pigpio.OUTPUT)
pi.set_mode(BUTTON_PIN,pigpio.INPUT)
pi.set_pull_up_down(BUTTON_PIN,pigpio.PUD_UP)
i2c = busio.I2C(board.SCL, board.SDA)
ser = serial.Serial('/dev/ttyUSB0', 9600)
sensor = adafruit_bno055.BNO055_I2C(i2c)


heading = 0.0
dis = 0.0
value = 360
count = 0
increment    = False
logic = False
flag = True
init = True
left = 0
data = ((ser.readline().decode('utf-8',errors='ignore').rstrip()))
try:
    dis, distanceRight = map(float, data.split(','))
except:
    dis = distanceRight = 0
print(dis,distanceRight)
time.sleep(3)

try:
    while pi.read(BUTTON_PIN) == 1:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Program Intrupt")
    exit()


while count<3:
    heading, _, __ = sensor.euler
    try:
        heading = min(360,max(0,heading))
    except:
        heading = 0
    data = ((ser.readline().decode('utf-8',errors='ignore').rstrip()))
    try:
        dis, distanceRight = map(float, data.split(','))
    except:
        dis = distanceRight = 0
    if left == 1:
        value,logic,flag,increment,count = l.L_journey(heading, dis, value, logic, flag, increment,count,init)
        left = 1
        init = False
        print("LeftRunning")
    elif left == 2:
        value,logic,flag,increment,count = r.R_journey(heading, distanceRight, value, logic, flag, increment,count,init)
        left = 2
        print("RRunning")
        init = False
    elif (dis>distanceRight and dis>100):
        value,logic,flag,increment,count = l.L_journey(heading, dis, value, logic, flag, increment,count,init)
        left = 1
        init = False
        print("LeftRunning")
    elif (dis<distanceRight and distanceRight>100):
        value,logic,flag,increment,count = r.R_journey(heading, distanceRight, value, logic, flag, increment,count,init)
        left = 2
        print("RRunnnning")
        init = False
    else:
        l.move(heading, value)
        print("NormalMove")
    key = cv2.waitKey(1)
    if key == ord('Q') or key == ord('q'):
        break
l.move(heading, value)
time.sleep(0.1)
pi.set_servo_pulsewidth(13,0)
