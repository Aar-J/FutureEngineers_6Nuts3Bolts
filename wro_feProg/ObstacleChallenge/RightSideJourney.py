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

# PID controller function for steering
def pid(y, heading, kP):
    # Normalize angles to the range [-180, 180]
    if (y < 360 - y):
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

    # Calculate the error between current heading and desired angle
    if heading < 0 and y < 0:
        error = heading - y
    elif heading < 0 and y > 0:
        error = y + heading
    else:
        error = heading - y

    # Calculate the servo position based on the error
    turn = min(2000, max(1000, 1500 - error * kP))
    return turn

def main(picam2, pi, sensor):
    # Initialize variables
    heading = roll = pitch = dis = 0.0
    value = 0
    count = 2  # Start count
    arR = arG = yy = xg = xr = 0
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

    while count < 3:
        # Capture image from the camera
        img = picam2.capture_array()
        img1 = img2 = img3 = img
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert image color space

        # Define color ranges for detection
        lower = (100, 70, 40)
        upper = (145, 255, 175)

        # Detect colors using functions from Blue_detected module
        img1, arR, xr, yr = b1.red_detect(img)
        img2, arG, xg, yg = b1.green_detect(img)
        img3, __, __, yy2, h1 = b1.color_detect(img, lower, upper, "blue")
        img3, ____, xO, yy, h2 = b1.color_detect(img, np.array([5, 80, 100]), np.array([30, 255, 255]), "orange")

        # Set yy based on xO detection
        yy = yy if xO < 340 else 0

        # Draw a rectangle on the image for visual feedback
        img = cv2.rectangle(img, (0, 100), (640, 350), (255, 255, 255), 2)
        cv2.imshow("frame", img)  # Display the processed frame

        # Get heading, roll, and pitch from the sensor
        heading, roll, pitch = sensor.euler
        
        try:
            heading = min(360, max(0, heading))  # Normalize heading
        except:
            heading = 0  # Default to 0 if there's an error
        
        # Try to read distance data from serial
        try:
            dis, distanceRight = map(float, data.split(','))
        except:
            dis = distanceRight = 0  # Default to 0 if there's an error
        
        # Check for orange color detection
        if (yy > 100 and yy < 320):
            orng1 = True
            print("orng1")
        elif yy > turnThreshold and orng1:
            orng2 = True
            print("orng2")

        # Set blue detection flag if both orange conditions are met
        if orng1 and orng2 and yy2 != 0:
            blue = True
            print("Blue is true")

        # Control logic based on red and green detection
        if (arR >= 3000 and yr >= 10 and yr > yy) or (arG >= 3000 and yg >= 10 and yg > yy):
            if(int(heading) in range(value, value + 60)):
                flag = True
                blue = False
                
            # Handle red detection
            if arR > arG:
                if(yr > 120):
                    pi.set_servo_pulsewidth(18, 1800)  # Turn right
                    print("Red_Turning")
                elif(yr > 40):
                    pi.set_servo_pulsewidth(18, max(1000, min(2000, 1500 + (320 - xr) * (-2))))
                    print("Red_Gliding")
                RedB4Turn = True
                if blue:
                    redAfterLine = True
                    redAtTurn = True
                    greenAfterLine = False
                else:
                    redAtTurn = False
                    
            # Handle green detection
            elif arR < arG:
                if(yg > 120):
                    pi.set_servo_pulsewidth(18, 1200)  # Turn left
                    print("Green_Turning")
                elif(yg > 40):
                    pi.set_servo_pulsewidth(18, max(1000, min(2000, 1500 + (320 - xg) * (-2))))
                    print("Green_Gliding")
                RedB4Turn = False
                if blue:
                    greenAfterLine = True
                    redAtTurn = False
                    redAfterLine = False

        # Handle blue detection logic
        elif blue:
            if(flag):
                value += 90
                if value == 360:
                    value = 0
                    increment = True
                
                if value == 0 and count == 1:
                    s_time = time.time()
                flag = False
                
            if(int(heading) not in range(value, value + 60)):
                orng1 = orng2 = False
                print("turning", heading, value, dis, RedB4Turn)
                if (arR > 3000 and arG < arR) or redAfterLine:
                    print("redBased")
                    redAfterLine = True
                    greenAfterLine = False
                    if heading >= 330 and value == 90:
                        pi.set_servo_pulsewidth(18, max(1000, min(2000, 1500 + (value - (heading - 360)) * 30)))
                    elif value == 0 and heading >= 230:
                        pi.set_servo_pulsewidth(18, max(1000, min(2000, 1500 + (value - (heading - 360)) * 30)))
                    else:
                        pi.set_servo_pulsewidth(18, max(1000, min(2000, 1500 + (value - heading) * 30)))  

                elif arG > 3000 and arG > arR or greenAfterLine:
                    print("greenBased")
                    redAfterLine = False
                    greenAfterLine = True
                    if heading >= 300 and value == 90:
                        pi.set_servo_pulsewidth(18, max(1050, min(1800, 1500 + (value - (heading - 360)) * 19)))
                    elif value == 0 and heading >= 230:
                        pi.set_servo_pulsewidth(18, max(1050, min(1800, 1500 + (value - (heading - 360)) * 19)))
                    else:
                        pi.set_servo_pulsewidth(18, max(1050, min(1800, 1500 + (value - heading) * 19)))
                    
                else:
                    redAfterLine = False
                    greenAfterLine = False
                    if heading >= 330 and value == 90:
                        pi.set_servo_pulsewidth(18, max(1000, min(1950, 1500 + (value - (heading - 360)) * 22)))
                    elif value == 0 and heading >= 230:
                        pi.set_servo_pulsewidth(18, max(1000, min(1950, 1500 + ((value) - (heading - 360)) * 22)))
                    else:
                        pi.set_servo_pulsewidth(18, max(1000, min(1950, 1500 + (value - heading) * 22)))
        
            else:
                print("Heading in range")
                blue = False
                orng1 = orng2 = False

        else:
            # Reset flags and increment count
            flag = True
            if increment:
                count = count + 1
                increment = False
            redAfterLine = greenAfterLine = False

            # Use PID to control servo position
            pi.set_servo_pulsewidth(18, pid(value, heading, 30))
            print(heading, dis, value, orng1, orng2, yy)
            
        # Set the pulse width for steering servo to 1550 microseconds
pi.set_servo_pulsewidth(13, 1550)

# Check for key press events
key = cv2.waitKey(1)  # Wait for 1 millisecond for a key event
# Break the loop if the 'q' key is pressed
if key == 1 or key == ord('q'):
    break

# Use PID controller to adjust drive motors based on the current heading and target value
pi.set_servo_pulsewidth(18, pid(value, heading, 30))
# Pause for a short time to allow the servo to respond
time.sleep(0.2)

print("Parking")  # Log the parking action

# Call the parking function from the P module, passing necessary parameters
P.main(pi, picam2, sensor, not(invert))

# Adjust servo 18's position again based on PID control
pi.set_servo_pulsewidth(18, pid(value, heading, 30))
# Pause for another short time
time.sleep(0.2)

# Set logic to False (likely used to control flow or state management)
logic = False

# Set pulse widths for both servos to 0, stopping them
pi.set_servo_pulsewidth(13, 0)
pi.set_servo_pulsewidth(18, 0)

# Clean up: close all OpenCV windows
cv2.destroyAllWindows()

# Stop the camera preview
picam2.stop()

# Stop the pigpio library, releasing resources
pi.stop()
