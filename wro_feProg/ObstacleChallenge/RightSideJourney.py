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
import parking1 as P
import Blue_detected as b1



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

def main(picam2, pi, sensor):
    heading = 0.0
    roll = 0.0
    pitch =0.0
    dis = 0.0
    value = 0
    count = 2 #NEED TO CHANGE IT BACK TO0
    arR = arG = yy= xg = xr = 0
    blue = False
    flag = True
    increment = False
    RedB4Turn = False
    orng1 = True
    orng2 = False
    turnThreshold = 350
    redAfterLine = greenAfterLine = False
    s_time = t_time = 0
    cross = False
    invert = False
    redAtTurn = False
    while count<3:
        #try:
        img=picam2.capture_array()
        img1 =img2 = img3 = img
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #     img = cv2.flip(img,-1)
        lower = (100,70,40)
        upper = (145,255,175)
        img1,arR,xr,yr = b1.red_detect(img)
    #     img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
        img2,arG,xg,yg = b1.green_detect(img)
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img3,__,__,yy2,h1 = b1.color_detect(img, lower,upper,"blue")
        img3,____,xO,yy,h2 = b1.color_detect(img, np.array([5,80,100]),np.array([30,255,255]),"orange")
        if xO<340:
            yy = yy
        else:
            yy = 0
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #yy2 = yy2 + h2
        img  = cv2.rectangle(img, (0,100), (640,350), (255,255,255), 2)
        cv2.imshow("frame",img)
    #     arR = arG = yr = yg = yy = yy2 = 0
    #     blue1 = blue2 = False
        heading, roll, pitch = sensor.euler
        
        try:
            heading = min(360,max(0,heading))
        except:
            heading = 0
        #data = ((ser.readline().decode('utf-8',errors='ignore').rstrip()))
        try:
            dis, distanceRight = map(float, data.split(','))
        except:
            dis = distanceRight = 0
        
    #     if RedB4Turn:
    #         turnThreshold = 340
    #     else:
    #         turnThreshold = 420
            
        if (yy>100 and yy <320):# or (yy2>100 and yy2<250):
            orng1 = True
            print("orng1")
    # or yy2>400:
        elif yy>turnThreshold and orng1:
            orng2 = True
            print("orng2")
            
        
        if orng1 and orng2 and yy2!=0:
            blue = True
            print("Blue is true")
        
        if (arR>=3000 and yr >= 10 and yr>yy) or (arG>=3000 and yg >= 10 and yg>yy):
            #flag = True
            if(int(heading) in range(value,value+60)):
                flag = True
                blue = False
                
            if arR>arG:
                if(yr>120):
                    pi.set_servo_pulsewidth(18,1800)
                    print("Red_Turning")
                elif(yr>40):
                    pi.set_servo_pulsewidth(18,max(1000,min(2000,1500 + (320-xr)*(-2))))
                    print("Red_Gliding")
                RedB4Turn = True
                if blue:
                    redAfterLine = True
                    redAtTurn = True
                    greenAfterLine = False
                else:
                    redAtTurn = False
                    
    #             r_crossed = True
                
            elif arR<arG:
                if(yg>120):
                    pi.set_servo_pulsewidth(18,1200)
                    print("Green_Turning")
                elif(yg>40):
                    pi.set_servo_pulsewidth(18,max(1000,min(2000,1500 + (320-xg)*(-2))))
                    print("Green_Gliding")
                RedB4Turn = False
                if blue:
                    greenAfterLine = True
                    redAtTurn = False
                    redAfterLine = False
                #g_crossed = True

        elif blue:
            if(flag):
                value +=90
                if value == 360:
                    value = 0
                    increment = True
                
                if value == 0 and count == 1:
                    s_time = time.time()
                flag = False
                
            if(int(heading) not in range(value,value+60)):
                orng1 = orng2 = False
                print("turning", heading, value, dis, RedB4Turn)
                if (arR>3000 and arG<arR) or redAfterLine:
                    print("redBased")
                    redAfterLine = True
                    greenAfterLine = False
                    if heading >=330 and value == 90:
                        pi.set_servo_pulsewidth(18,max(1000,min(2000,1500 + (value-(heading-360))*30)))
                    elif value ==  0 and heading>=230:
                        pi.set_servo_pulsewidth(18,max(1000,min(2000,1500 + (value-(heading-360))*30)))
                    else:
                        pi.set_servo_pulsewidth(18,max(1000,min(2000,1500 + (value-heading)*30)))  
                    

                elif arG>3000 and arG>arR or greenAfterLine:
                    print("greenBased")
                    redAfterLine  = False
                    greenAfterLine = True
                    if heading >=300 and value == 90:
                        pi.set_servo_pulsewidth(18,max(1050,min(1800,1500 + (value-(heading-360))*19)))
                    elif value ==  0 and heading>=230:
                        pi.set_servo_pulsewidth(18,max(1050,min(1800,1500 + (value-(heading-360))*19)))
                    else:
                        pi.set_servo_pulsewidth(18,max(1050,min(1800,1500 + (value-heading)*19)))
                    
                else:
                    redAfterLine  = False
                    greenAfterLine = False
                    if heading >=330 and value == 90:
                        pi.set_servo_pulsewidth(18,max(1000,min(1950,1500 + (value-(heading-360))*22)))
                    elif value ==  0 and heading>=230:
                        pi.set_servo_pulsewidth(18,max(1000,min(1950,1500 + ((value)-(heading-360))*22)))
                    else:
                        pi.set_servo_pulsewidth(18,max(1000,min(1950,1500 + (value-heading)*22)))
        
              #  pi.set_servo_pulsewidth(13,1530)
            else:
                 print("Heading in range")
                 blue = False
                 orng1 = orng2 = False

        else:
            
            flag = True
            if increment:

                count = count + 1
                increment = False
            redAfterLine = greenAfterLine = False

            pi.set_servo_pulsewidth(18,pid(value,heading,30))
            print(heading,dis, value, orng1, orng2, yy)
            
        pi.set_servo_pulsewidth(13,1550)
        
        if count == 2 and value == 0 and (heading<40 or heading>350) and (int(time.time()%100 - s_time%100)<=3):
            print("InConditionhgfghjkhgfghjkjhgfghjkjhgfd")
            if RedB4Turn:
                print("Inverted!")
                invert = True
                if redAtTurn or yr>=100:
                    cross = True
                
                break
            
        key = cv2.waitKey(1)
        if key == 1 or key == ord('q'):
            break

    if cross:
        pi.set_servo_pulsewidth(18,pid(value,heading,30))
        time.sleep(0.1)
    while invert:
        heading, roll, pitch = sensor.euler
        
        try:
            heading = min(360,max(0,heading))
        except:
            heading = 0
        if cross:
            if heading<60 or heading>320:
                pi.set_servo_pulsewidth(18,1250)
            elif heading>180:
                pi.set_servo_pulsewidth(18,pid(180,heading,30))
            else:
                break
        else:
            if heading<90 or heading>350:
                pi.set_servo_pulsewidth(18,1100)
                pi.set_servo_pulsewidth(13,1450)
            else:
                break
        
        key = cv2.waitKey(1)
        if key == 1 or key == ord('q'):
            break
    count = 0
    blue1 = True
    blue2 = False
    orange= False
    if cross:
        value = 180
    else:
        value = 90
    while count<1 and invert:
        #try:
        img=picam2.capture_array()
        img1 =img2 = img3 = img
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #     img = cv2.flip(img,-1)
        lower = (100,70,40)
        upper = (145,255,175)
        img1,arR,xr,yr = b1.red_detect(img)
    #     img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
        img2,arG,xg,yg = b1.green_detect(img)
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img3,__,xB,yy,h1 = b1.color_detect(img, lower,upper,"blue")
        if xB>300:
            yy = yy
        else:
            yy = 0
        img3,__,_____,yy2,h2 = b1.color_detect(img, np.array([11,100,50]),np.array([30,255,255]),"orange")
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #yy2 = yy2 + h2
        img  = cv2.rectangle(img, (0,100), (640,320), (255,255,255), 2)
        cv2.imshow("frame",img)
    #     arR = arG = yr = yg = yy = yy2 = 0
    #     blue1 = blue2 = False
        heading, roll, pitch = sensor.euler
        
        try:
            heading = min(360,max(0,heading))
        except:
            heading = 0
        #qqqqqqqqdata = ((ser.readline().decode('utf-8',errors='ignore').rstrip()))
        try:
            dis, distanceRight = map(float, data.split(','))
        except:
            dis = distanceRight = 0
        
    #     if RedB4Turn:
    #         turnThreshold = 340
    #     else:
    #         turnThreshold = 420
            
        if (yy>100 and yy <320):# or (yy2>100 and yy2<250):
            blue1 = True
            print("blue1")
    # or yy2>400:
        elif yy>turnThreshold and blue1:
            blue2 = True
            print("blue2")
            
        
        if blue1 and blue2 and yy2!=0:
            orange = True
            print("Orange is true")
        
        if (arR>=3000 and yr >= 10 and yr>yy) or (arG>=3000 and yg >= 10 and yg>yy):
            #flag = True
            if(int(heading) in range(value-60,value+5)):
                flag = True
                orange = False
                
            if arR>arG:
                if(yr>80):
                    pi.set_servo_pulsewidth(18,1850)#turn(heading, 40)
                    print("Red_Turning")
                elif(yr>40):
                    pi.set_servo_pulsewidth(18,max(1000,min(2000,1500 + (320-xr)*(-1))))
                    print("Red_Gliding")
                RedB4Turn = True
                if orange:
                    redAfterLine = True
                    
    #             r_crossed = True
                
            elif arR<arG:
                if(yg>80):
                    pi.set_servo_pulsewidth(18,1150)
                    print("Green_Turning")
                elif(yg>40):
                    pi.set_servo_pulsewidth(18,max(1000,min(2000,1500 + (320-xg)*(-1))))
                    print("Green_Gliding")
                RedB4Turn = False
                #g_crossed = True
                
           # pi.set_servo_pulsewidth(13,1560)

                
            #print(dis, distanceRight)
        elif orange:
            if(flag):
                value -=90
                if value == 0:
                    value = 360
                elif value == 180:
                    increment = True            
                flag = False
                
            if(int(heading) not in range(value-60,value+5)):
                blue1 = blue2 = False
                print("turning", heading, value, dis, RedB4Turn)
                if (arR>3000 and arG<arR) or redAfterLine:
                    print("redBased")
                    redAfterLine = True
                    greenAfterLine = False
                    if heading <=30 and value == 270:
                        pi.set_servo_pulsewidth(18,max(1200,min(1950,1500 + (value-(heading+360))*18)))
                    elif value ==  360 and heading<=120:
                        pi.set_servo_pulsewidth(18,max(1200,min(1950,1500 + ((value-360)-heading)*18)))
                    else:
                        pi.set_servo_pulsewidth(18,max(1200,min(1950,1500 + (value-heading)*18)))

                elif arG>3000 and arG>arR or greenAfterLine:
                    print("greenBased")
                    redAfterLine  = False
                    greenAfterLine = True
                    if heading <=30 and value == 270:
                        pi.set_servo_pulsewidth(18,max(1000,min(1950,1500 + (value-(360+heading))*30)))
                    elif value ==  360 and heading<=120:
                        pi.set_servo_pulsewidth(18,max(1000,min(1950,1500 + ((value-360)-heading)*30)))
                    else:
                        pi.set_servo_pulsewidth(18,max(1000,min(1950,1500 + (value-heading)*30)))  
                else:
                    redAfterLine  = False
                    greenAfterLine = False
                    if heading <=30 and value == 270:
                        pi.set_servo_pulsewidth(18,max(1200,min(1950,1500 + (value-(heading+360))*15)))
                    elif value ==  360 and heading<=120:
                        pi.set_servo_pulsewidth(18,max(1200,min(1950,1500 + ((value-360)-heading)*15)))
                    else:
                        pi.set_servo_pulsewidth(18,max(1200,min(1950,1500 + (value-heading)*15)))
        
                #pi.set_servo_pulsewidth(13,1540)
            else:
                 print("Heading in range")
                 orange = False
                 blue1 = blue2 = False

        else:
            
            flag = True
            if increment:
                count = count + 1
                increment = False
            redAfterLine = greenAfterLine = False

            pi.set_servo_pulsewidth(18,pid(value,heading,30))
            print(heading,dis, value, blue1, blue2, time.time()%100, count)
            
        pi.set_servo_pulsewidth(13,1550)

            
            
        key = cv2.waitKey(1)
        if key == 1 or key == ord('q'):
            break
        
    pi.set_servo_pulsewidth(18,pid(value,heading,30))
    time.sleep(0.2)
    print("Parking")
    P.main(pi, picam2, sensor, not(invert))

    pi.set_servo_pulsewidth(18,pid(value,heading,30))
    time.sleep(0.2)
    logic = False
    pi.set_servo_pulsewidth(13,0)
    pi.set_servo_pulsewidth(18,0)
    cv2.destroyAllWindows()
    picam2.stop()
    pi.stop()
