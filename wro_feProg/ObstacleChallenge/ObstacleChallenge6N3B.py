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
import Blue_detected as b1

# Initialize the camera
picam2 = Picamera2()
config = picam2.create_video_configuration(main={"size": (640, 480)}, controls={"FrameDurationLimits": (33333, 33333)})
picam2.configure(config)
picam2.start()

def pid(y, heading, kP):
    # Calculate the turn based on the PID control algorithm
    if y < 360 - y:
        y = y
    elif (y == 360 - y):
        y = 180
    else:
        y = -360 + y
    if (heading < 360 - heading):
        heading = heading
    elif (heading == 360 - heading):
        heading = 180
    else:
        heading = -360 + heading
    if heading < 0 and y < 0:
        error = heading - y
    elif heading < 0 and y > 0:
        error = y + heading
    else:
        error = heading - y
    turn = min(2000, max(1000, 1500 - error * kP))
    return turn

# Initialize pigpio and set GPIO pin modes
pi = pigpio.pi()
pi.set_mode(18, pigpio.OUTPUT)
pi.set_mode(13, pigpio.OUTPUT)

# Set up I2C and sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)
heading = 0.0
roll = 0.0
pitch = 0.0
dis = 0.0
value = 360
count = 1
arR = arG = yy = xg = xr = 0
orange = False
flag = True
increment = False
time.sleep(1)

# Initialize flags and thresholds
RedB4Turn = False
blue1 = blue2 = False
invert = False
turnThreshold = 340
redAfterLine = greenAfterLine = False
cross = False
s_time = 0

def turn(heading, tgt):
    # Function to control the turning based on heading and target
    pi.set_servo_pulsewidth(18, pid(tgt + heading, heading, 40))

while count < 3:
    img = picam2.capture_array()  # Capture image from camera
    img1 = img2 = img3 = img  # Create copies of the image for processing
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert image from BGR to RGB

    # Define color thresholds for detection
    lower = (100, 70, 40)
    upper = (145, 255, 175)

    # Detect colors using custom functions
    img1, arR, xr, yr = b1.red_detect(img)
    img2, arG, xg, yg = b1.green_detect(img)
    img3, __, xB, yy, h1 = b1.color_detect(img, lower, upper, "blue")

    if xB > 300:
        yy = yy
    else:
        yy = 0
    
    img3, __, ____, yy2, h2 = b1.color_detect(img, np.array([11, 100, 50]), np.array([30, 255, 255]), "orange")

    # Draw rectangle on image for visualization
    img = cv2.rectangle(img, (0, 100), (640, 320), (255, 255, 255), 2)
    cv2.imshow("frame", img)

    # Read heading, roll, and pitch from the sensor
    heading, roll, pitch = sensor.euler
    
    try:
        heading = min(360, max(0, heading))  # Normalize heading
    except:
        heading = 0

    # Attempt to read distance data
    try:
        dis, distanceRight = map(float, data.split(','))
    except:
        dis = distanceRight = 0

    # Check color detection and set flags accordingly
    if (yy > 100 and yy < 320):  # Check for blue detection
        blue1 = True
        print("blue1")
    elif yy > turnThreshold and blue1:
        blue2 = True
        print("blue2")
        
    if blue1 and blue2 and yy2 != 0:
        orange = True
        print("Orange is true")
    
    # Check for red or green detection and respond accordingly
    if (arR >= 3000 and yr >= 10 and yr > yy) or (arG >= 3000 and yg >= 10 and yg > yy):
        if(int(heading) in range(value - 60, value + 5)):
            flag = True
            orange = False
            
        if arR > arG:
            if (yr > 80):
                pi.set_servo_pulsewidth(18, 1850)  # Turn
                print("Red_Turning")
            elif (yr > 40):
                pi.set_servo_pulsewidth(18, max(1000, min(2000, 1500 + (320 - xr) * (-1))))  # Glide
                print("Red_Gliding")
            RedB4Turn = True
            if orange:
                redAfterLine = True
                
        elif arR < arG:
            if (yg > 80):
                pi.set_servo_pulsewidth(18, 1150)  # Turn
                print("Green_Turning")
            elif (yg > 40):
                pi.set_servo_pulsewidth(18, max(1000, min(2000, 1500 + (320 - xg) * (-1))))  # Glide
                print("Green_Gliding")
            RedB4Turn = False
            
    elif orange:
        if (flag):
            value -= 90  # Update target value
            if value == 0:
                value = 360
                increment = True            
            if value == 360 and count == 1:
                s_time = time.time()  # Record start time
            flag = False
            
        if(int(heading) not in range(value - 60, value + 5)):
            blue1 = blue2 = False
            print("turning", heading, value, dis, RedB4Turn)
            if (arR > 3000 and arG < arR) or redAfterLine:
                print("redBased")
                redAfterLine = True
                greenAfterLine = False
                if heading <= 30 and value == 270:
                    pi.set_servo_pulsewidth(18, max(1200, min(1950, 1500 + (value - (heading + 360)) * 18)))
                elif value == 360 and heading <= 120:
                    pi.set_servo_pulsewidth(18, max(1200, min(1950, 1500 + ((value - 360) - heading) * 18)))
                else:
                    pi.set_servo_pulsewidth(18, max(1200, min(1950, 1500 + (value - heading) * 18)))

            elif arG > 3000 and arG > arR or greenAfterLine:
                print("greenBased")
                redAfterLine  = False
                greenAfterLine = True
                if heading <= 30 and value == 270:
                    pi.set_servo_pulsewidth(18, max(1000, min(1950, 1500 + (value - (360 + heading)) * 30)))
                elif value == 360 and heading <= 120:
                    pi.set_servo_pulsewidth(18, max(1000, min(1950, 1500 + ((value - 360) - heading) * 30)))
                else:
                    pi.set_servo_pulsewidth(18, max(1000, min(1950, 1500 + (value - heading) * 30)))  
            else:
                redAfterLine  = False
                greenAfterLine = False
                if heading <= 30 and value == 270:
                    pi.set_servo_pulsewidth(18, max(1200, min(1950, 1500 + (value - (heading + 360)) * 15)))
                elif value == 360 and heading <= 120:
                    pi.set_servo_pulsewidth(18, max(1200, min(1950, 1500 + ((value - 360) - heading) * 15)))
                else:
                    pi.set_servo_pulsewidth(18, max(1200, min(1950, 1500 + (value - heading) * 15)))
    
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

        pi.set_servo_pulsewidth(18, pid(value, heading, 30))  # Set PID control outpu

        print(heading,dis, value, blue1, blue2, time.time()%100, count)
        
        pi.set_servo_pulsewidth(13,1550)  # Set servo pulse width for channel 13 to 1550

# Check conditions for inversion and crossing
if count == 2 and value == 360 and (heading < 40 or heading > 350) and (int(time.time() % 100 - s_time % 100) <= 4):
    print("InConditionhgfghjkhgfghjkjhgfghjkjhgfd")  # Debug message for condition
    if yr >= 20 or RedB4Turn:
        print("Inverted!")  # Indicate inversion state
        invert = True  # Set inversion flag
        if yr >= 100:
            cross = True  # Set crossing flag if yr condition is met
        break  # Exit the loop

# Wait for a key press
key = cv2.waitKey(1)  # Check for keyboard input
if key == 1 or key == ord('q'):  # Break on specific key press
    break

logic = False  # Initialize logic state
count = 0  # Reset count

# Check if crossing has been triggered
if cross:
    pi.set_servo_pulsewidth(18, pid(value, heading, 30))  # Adjust servo pulse width for channel 18
    time.sleep(0.1)  # Delay for a short duration

while invert:  # Continue while inverting
    heading, roll, pitch = sensor.euler  # Read sensor orientation data

    try:
        heading = min(360, max(0, heading))  # Normalize heading to be within [0, 360]
    except:
        heading = 0  # Default heading to 0 if there's an error

    # Check for specific heading range for crossing
    if cross:
        if int(heading) not in range(180, 185):  # Check if heading is not within 180-185
            print("HEADING", heading)  # Print current heading
            pi.set_servo_pulsewidth(18, pid(180, heading, 30))  # Adjust servo for crossing
        else:
            break  # Exit loop if in desired heading range
    else:
        # Control servo based on heading
        if heading > 270 or heading < 10:
            pi.set_servo_pulsewidth(18, 1900)  # Adjust for heading condition
            pi.set_servo_pulsewidth(13, 1450)  # Adjust for another condition
        else:
            break  # Exit loop if heading is within range

    key = cv2.waitKey(1)  # Wait for a key press
    if key == 1 or key == ord('q'):  # Break on specific key press
        break

# Final adjustments for servo pulse widths
pi.set_servo_pulsewidth(13, 0)  # Turn off servo on channel 13
pi.set_servo_pulsewidth(18, 0)  # Turn off servo on channel 18
cv2.destroyAllWindows()  # Close all OpenCV windows
picam2.stop()  # Stop the camera
pi.stop()  # Stop the pigpio interface
