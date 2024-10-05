import time
import board
import busio
import adafruit_bno055
import sys
import serial
import parking1 as P
sys.path.append('/usr/lib/python3/dist-packages')
import pigpio
from picamera2 import Picamera2, Preview
import cv2
import numpy as np
import Blue_detected as b1


def pid(y, heading, kP):
    # Calculate the error between desired heading (y) and current heading
    if y < 360 - y:
        y = y
    elif (y == 360 - y):
        y = 180
    else:
        y = -360 + y

    if heading < 360 - heading:
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

    turn = min(2000, max(1000, 1500 - error * kP))  # Calculate turn value
    return turn

def main(picam2, pi, sensor):
    heading = 0.0
    roll = 0.0
    pitch = 0.0
    dis = 0.0
    value = 360
    count = 0
    arR = arG = yy = xg = xr = 0
    orange = False
    flag = True
    increment = False
    RedB4Turn = False
    blue1 = blue2 = False
    invert = False
    turnThreshold = 340
    redAfterLine = greenAfterLine = False
    cross = False
    redAfterTurn = False
    s_time = 0

    while count < 3:
        # Capture image from the camera
        img = picam2.capture_array()
        img1 = img2 = img3 = img
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert image to RGB
        
        # Define color detection thresholds
        lower = (100, 70, 40)
        upper = (145, 255, 175)

        # Detect red, green, and blue colors
        img1, arR, xr, yr = b1.red_detect(img)
        img2, arG, xg, yg = b1.green_detect(img)
        img3, __, xB, yy, h1 = b1.color_detect(img, lower, upper, "blue")
        
        # Process blue detection
        if xB > 300:
            yy = yy
        else:
            yy = 0

        img3, __, __, yy2, h2 = b1.color_detect(img, np.array([11, 100, 50]), np.array([30, 255, 255]), "orange")
        yy2 = yy2 + h2
        
        # Draw a rectangle on the image for visual reference
        img = cv2.rectangle(img, (0, 100), (640, 320), (255, 255, 255), 2)
        cv2.imshow("frame", img)  # Display the processed image

        heading, roll, pitch = sensor.euler  # Get heading, roll, and pitch from sensor
        
        # Normalize heading value
        try:
            heading = min(360, max(0, heading))
        except:
            heading = 0
        
        # Check distance readings (assuming `data` is defined elsewhere)
        try:
            dis, distanceRight = map(float, data.split(','))
        except:
            dis = distanceRight = 0

        # Detect conditions for turning
        if (yy > 100 and yy < 320):
            blue1 = True
            print("blue1")
        elif yy > turnThreshold and blue1:
            blue2 = True
            print("blue2")
        
        # Set orange flag if conditions are met
        if blue1 and blue2 and yy2 != 0:
            orange = True
            print("Orange is true")
        
        # Check for red or green detected
        if (arR >= 3000 and yr >= 10 and (yr > yy2 if (yy == 0) else yr > yy)) or (arG >= 3000 and yg >= 10 and (yg > yy2 if (yy == 0) else yg > yy)):
            if(int(heading) in range(value - 60, value + 5)):
                flag = True
                orange = False
            
            if arR > arG:
                if(yr > 80):
                    pi.set_servo_pulsewidth(18, 1800)  # Turn for red detected
                    print("Red_Turning")
                elif(yr > 10):
                    pi.set_servo_pulsewidth(18, max(1000, min(2000, 1500 + (320 - xr) * (-1))))
                    print("Red_Gliding")
                RedB4Turn = True
                
                if orange:
                    redAfterLine = True
                    redAfterTurn = True
                else:
                    redAfterTurn = False
                    
            elif arR < arG:
                if(yg > 80):
                    pi.set_servo_pulsewidth(18, 1200)  # Turn for green detected
                    print("Green_Turning")
                elif(yg > 10):
                    pi.set_servo_pulsewidth(18, max(1000, min(2000, 1500 + (320 - xg) * (-1))))
                    print("Green_Gliding")
                RedB4Turn = False

        elif orange:
            if flag:
                value -= 90
                if value == 0:
                    value = 360
                    increment = True            
                if value == 360 and count == 1:
                    s_time = time.time()  # Record start time for condition checking
                flag = False
                
            if(int(heading) not in range(value - 60, value + 5)):
                blue1 = blue2 = False
                print("turning", heading, value, dis, RedB4Turn)
                
                # Control logic for red and green based on heading
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

                elif (arG > 3000 and arG > arR) or greenAfterLine:
                    print("greenBased")
                    redAfterLine = False
                    greenAfterLine = True
                    
                    if heading <= 30 and value == 270:
                        pi.set_servo_pulsewidth(18, max(1000, min(1950, 1500 + (value - (360 + heading)) * 30)))
                    elif value == 360 and heading <= 120:
                        pi.set_servo_pulsewidth(18, max(1000, min(1950, 1500 + ((value - 360) - heading) * 30)))
                    else:
                        pi.set_servo_pulsewidth(18, max(1000, min(1950, 1500 + (value - heading) * 30)))
                else:
                    redAfterLine = False
                    greenAfterLine = False
                    
                    if heading <= 30 and value == 270:
                        pi.set_servo_pulsewidth(18, max(1000, min(1950, 1500 + (value - (heading + 360)) * 28)))
                    elif value == 360 and heading <= 120:
                        pi.set_servo_pulsewidth(18, max(1000, min(1950, 1500 + ((value - 360) - heading) * 28)))
                    else:
                        pi.set_servo_pulsewidth(18, max(1000, min(1950, 1500 + (value - heading) * 28)))
        
            else:
                print("Heading in range")
                orange = False
                blue1 = blue2 = False

        else:
            flag = True
            if increment:
                count += 1  # Increment count if conditions met
                increment = False
            redAfterLine = greenAfterLine = False

            pi.set_servo_pulsewidth(18, pid(value, heading, 30))  # PID control
            print(heading, dis, value, blue1, blue2, time.time() % 100, count)
            
        pi.set_servo_pulsewidth(13, 1550)  # Control another servo

        # Check for keyboard input
key = cv2.waitKey(1)
# Exit loop if 'q' is pressed or if a specific key is detected
if key == 1 or key == ord('q'):
    break

# Set servo pulse width for parking maneuver based on PID controller output
pi.set_servo_pulsewidth(18, pid(value, heading, 30))
# Introduce a short delay to allow for stabilization
time.sleep(0.2)

# Indicate that the parking process is starting
print("Parking")

# Execute the parking routine from the parking module
P.main(pi, picam2, sensor, invert)

# Reset servo positions to zero after parking
pi.set_servo_pulsewidth(13, 0)
pi.set_servo_pulsewidth(18, 0)

# Clean up by closing all OpenCV windows
cv2.destroyAllWindows()

# Stop the camera and clean up the GPIO
picam2.stop()
pi.stop()
