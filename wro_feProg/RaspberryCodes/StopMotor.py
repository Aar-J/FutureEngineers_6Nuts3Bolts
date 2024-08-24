import pigpio
from time import sleep

pi = pigpio.pi()
pi.set_mode(18, pigpio.OUTPUT)
pi.set_mode(13,pigpio.OUTPUT)
pi.set_servo_pulsewidth(18,1200)
pi.set_servo_pulsewidth(13,1500)
sleep(0.1)