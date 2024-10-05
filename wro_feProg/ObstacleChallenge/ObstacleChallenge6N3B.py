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
import numpy as np
import ObbstacleChallenge as L
import InvertedObstacleChallenge as R
import Blue_detected as b1

picam2 = Picamera2()
config = picam2.create_video_configuration( main={"size": (640, 480)},controls={"FrameDurationLimits": (33333, 33333)})
picam2.configure(config)


picam2.start()

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
sensor = adafruit_bno055.BNO055_I2C(i2c)
heading = 0.0
roll = 0.0
pitch =0.0
dis = 0.0
value = 0
yy=yy2 =0
while yy==0 and yy2==0:#:yy==0 or yy2 == 0:
    img=picam2.capture_array()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img[0:240,0:640,0:3] = 255
    lower = (100,70,40)
    upper = (145,255,175)
    img,arR,xr,yr = b1.red_detect(img)
    img,arG,xg,yg = b1.green_detect(img)
    img,__,xB,yy,h1 = b1.color_detect(img, lower,upper,"blue")
    img,__,_____,yy2,h2 = b1.color_detect(img, np.array([11,100,50]),np.array([30,255,255]),"orange")
    cv2.imshow("frame",img)

    heading, roll, pitch = sensor.euler
    
    try:
        heading = min(360,max(0,heading))
    except:
        heading = 0
    
    if (arR>=3000 and yr >= 10) or (arG>=3000 and yg >= 10):

            
        if arR>arG:
            if(yr>80):
                pi.set_servo_pulsewidth(18,1800)#turn(heading, 40)
                print("Red_Turning")
            elif(yr>10):
                pi.set_servo_pulsewidth(18,max(1000,min(2000,1500 + (320-xr)*(-1))))
                print("Red_Gliding")           
        elif arR<arG:
            if(yg>80):
                pi.set_servo_pulsewidth(18,1200)
                print("Green_Turning")
            elif(yg>10):
                pi.set_servo_pulsewidth(18,max(1000,min(2000,1500 + (320-xg)*(-1))))
                print("Green_Gliding")
    else:
        pi.set_servo_pulsewidth(18,pid(value,heading,30))
        
    pi.set_servo_pulsewidth(13,1550)
    
    key = cv2.waitKey(1)
    if key == 1 or key == ord('q'):
        break
# pi.set_servo_pulsewidth(13,0)
pi.set_servo_pulsewidth(18,0)
print(yy,yy2)
time.sleep(0.2)
if yy2>=yy:
    print("RightSideJourney")
    R.main(picam2, pi, sensor)
elif yy>yy2:
    print("LeftSideJourney")
    L.main(picam2, pi, sensor)
elif yy==0 and yy2==0:
    print("NOne")
else:
    print(yy,yy2,"Nil")
pi.set_servo_pulsewidth(13,0)
pi.set_servo_pulsewidth(18,0)
cv2.destroyAllWindows()
picam2.stop()
pi.stop()
