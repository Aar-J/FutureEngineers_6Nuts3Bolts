import pigpio
import time
import pygame

pi = pigpio.pi()
pygame.init()
#pygame.joystick().init()

pi.set_mode(13, pigpio.OUTPUT)
pi.set_mode(18, pigpio.OUTPUT)
js = pygame.joystick.Joystick(0)
js.init()
while True:
    pygame.event.pump()
    axis = -js.get_axis(1)#left joystick y axis 
    axis2 = js.get_axis(3)# right joystick x axis
    if axis >= 0.1 or axis <= -0.1:
        print("")
        #pi.set_servo_pulsewidth(13,(1500+(axis*500)*0.2)) #1500 is stop, lower is clockwise and higher is anticlockwise
    else:
        pi.set_servo_pulsewidth(13,1500) #1500 is stop, lower is clockwise and higher is anticlockwise
    
    if axis2 >= 0.1 or axis2 <= -0.1:
        #pi.set_servo_pulsewidth(18,(1350+axis2*350))
        pi.set_servo_pulsewidth(18,(1200+axis2*400))
    else:
        #pi.set_servo_pulsewidth(18, 1350)
        pi.set_servo_pulsewidth(18, 1200)
    print(f"X axis is - {axis:.2f} y is - {axis2:.2f}")
pi.stop()
