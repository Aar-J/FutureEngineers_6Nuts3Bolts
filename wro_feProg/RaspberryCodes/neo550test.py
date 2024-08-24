import pigpio
from time import sleep

pi = pigpio.pi()
pi.set_mode(18, pigpio.OUTPUT)
pigpio.clear()

pi.set_servo_pulsewidth(18, 1200)
sleep(2)
pi.set_servo_pulsewidth(18, 1800)
sleep(2)