import time
import board
import busio
import adafruit_bno055
import sys
import serial
sys.path.append('/usr/lib/python3/dist-packages')  # Add system package path
import pigpio
from picamera2 import Picamera2, Preview  # Import for camera control
import cv2

# PID control function to calculate turn values based on heading and target
def pid(y, heading, kP):
    # Normalize the target value (y)
    if (y < 360 - y):
        y = y
    elif (y == 360 - y):
        y = 180
    else:
        y = -360 + y
    
    # Normalize the heading value
    if (heading < 360 - heading):
        heading = heading
    elif (heading == 360 - heading):
        heading = 180
    else:
        heading = -360 + heading
    
    # Calculate the error between heading and target
    if heading < 0 and y < 0:
        error = heading - y
    elif heading < 0 and y > 0:
        error = y + heading
    else:
        error = heading - y
    
    # Calculate turn value using PID (Proportional control)
    turn = min(1600, max(800, 1200 - error * kP))  # Bound the turn value between 800 and 1600
    return turn

# Initialize pigpio
pi = pigpio.pi()

# Set GPIO modes for motor and servo
pi.set_mode(18, pigpio.OUTPUT)  # Drive motor on GPIO pin 18
pi.set_mode(13, pigpio.OUTPUT)  # Steering servo on GPIO pin 13

# Initialize I2C for BNO055 sensor and Serial communication
i2c = busio.I2C(board.SCL, board.SDA)  # I2C bus for BNO055
ser = serial.Serial('/dev/ttyACM0', 9600)  # Serial communication on USB port
sensor = adafruit_bno055.BNO055_I2C(i2c)  # BNO055 sensor initialization over I2C

# Variables to store sensor and journey states
heading = 0.0  # Robot's heading (angle)
roll = 0.0  # Placeholder for roll angle
pitch = 0.0  # Placeholder for pitch angle
dis = 0.0  # Distance traveled (placeholder)
value = 0  # Target heading or angle
count = 0  # Counter for the journey progress
increment = False  # Flag to manage increments in movement steps
logic = False  # Logic flag for journey management
flag = True  # General-purpose flag

time.sleep(3)  # Delay before starting the main process

# Right journey function that adjusts the robot's movement based on heading and distance data
def R_journey(heading, distanceRight, value, logic, flag, increment, count, init):
    if init:  # Initialize journey variables
        value = 0
        count = 0
        increment = False
        logic = False
        flag = True
        init = False
        print("Initializeeeeeeeeeed")
    
    # If the robot has traveled more than 120 units or logic is True
    if (distanceRight >= 120 or logic):
        if flag:  # On first run, adjust the value (angle)
            value += 90  # Increment by 90 degrees
            if value == 360:  # Reset to 0 if full circle is reached
                value = 0
                increment = True  # Allow increment in count
            flag = False  # Turn off the flag after adjustment
        
        # If the heading is outside the acceptable range, adjust the steering
        if heading not in range(value - 5, value + 60):
            print("Turning", heading, value, distanceRight)  # Debug info
            
            # Specific case when heading is near the upper boundary
            if heading >= 350 and value == 90:
                pi.set_servo_pulsewidth(18, 1500)  # Set motor pulse width for turning
            elif value == 0 and heading >= 260:
                # Condition for adjusting motor pulse width in boundary cases
                pi.set_servo_pulsewidth(18, max(950, min(1550, 1200 + (value - heading + 360) * 18)))
                print("Condition b")
            else:
                # Regular case for turning based on heading
                pi.set_servo_pulsewidth(18, max(950, min(1550, 1200 + (value - heading) * 18)))
            
            pi.set_servo_pulsewidth(13, 1570)  # Steering servo control
            logic = True  # Indicate that turning is in process
        else:
            # Once within the acceptable heading range, move forward
            pi.set_servo_pulsewidth(18, 1200)  # Set drive motor to constant speed
            pi.set_servo_pulsewidth(13, 1570)  # Steering is straight
            logic = False  # Reset the logic flag after turn is complete
            time.sleep(0.08)  # Short delay to stabilize movement
    
    else:
        # If no major turning or distance requirement, proceed normally
        flag = True  # Reset the flag for the next round
        if increment:  # If increment flag is set, update the count
            count += 1
            increment = False  # Reset the increment flag
        
        print(heading, distanceRight, value)  # Debug information
        
        # Use PID to adjust the motor's turning based on heading and target
        pi.set_servo_pulsewidth(18, pid(value, heading, 20))  # PID control for motor
        pi.set_servo_pulsewidth(13, 1570)  # Keep steering straight
    
    return value, logic, flag, increment, count  # Return updated variables to maintain state
