import pigpio
from time import sleep
from gpiozero import DistanceSensor
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

ulLeft = DistanceSensor(echo=17, trigger=4)
ulRight = DistanceSensor(echo=23, trigger=5)
threshLeft = 50
threshRight = 10
kp = 0.5
centerpos = 1750

pi = pigpio.pi()
pi.set_mode(18, pigpio.OUTPUT)
pi.set_mode(12, pigpio.OUTPUT)

while True:
    data = ser.readline().decode('utf-8').rstrip()
    if (ulLeft.distance*100) < threshLeft:
        if (ulRight.distance*100) < threshRight: #(Robot near wall)
            error = ulRight.distance*100 - threshRight #Negative Value 
            newpos = centerpos + (kp*error)
            pi.set_servo_pulsewidth(18, newpos)
            sleep(0.1)
        else: #Robot far from wall
            error = ulRight.distance*100 - threshRight #Positive Value 
            newpos = centerpos + (kp*error)
            pi.set_servo_pulsewidth(18, newpos)
            sleep(0.1)
    pi.set_servo_pulsewidth(12,1400)