# Import required libraries and modules
import time
import board
import busio
import adafruit_bno055
import sys
import serial
sys.path.append('/usr/lib/python3/dist-packages')  # Path for required Python packages
import pigpio  # For controlling servos via GPIO
from picamera2 import Picamera2, Preview  # For camera control (unused in this code)
import cv2

# Function to implement a Proportional-Integral-Derivative (PID) controller
# for adjusting the robot's movement
def pid(y, heading, kP):
    # Adjust 'y' (target value) based on its proximity to 360 degrees
    if (y < 360 - y):
        y = y
    elif (y == 360 - y):
        y = 180
    else:
        y = -360 + y

    # Adjust 'heading' (current direction) similarly
    if (heading < 360 - heading):
        heading = heading
    elif (heading == 360 - heading):
        heading = 180
    else:
        heading = -360 + heading

    # Calculate the error (difference between target and current direction)
    if heading < 0 and y < 0:
        error = heading - y
    elif heading < 0 and y > 0:
        error = y + heading
    else:
        error = heading - y

    # Calculate the turn value using the error and proportional constant (kP)
    turn = min(2000, max(1000, 1500 - error * kP))  # Constrain turn value between 1000 and 2000
    return turn

# Initialize pigpio for controlling GPIO pins
pi = pigpio.pi()

# Set GPIO pin 18 for controlling the drive motor and 13 for steering
pi.set_mode(18, pigpio.OUTPUT)  # Drive motor
pi.set_mode(13, pigpio.OUTPUT)  # Steering servo

# Initialize I2C bus for the BNO055 sensor and serial communication
i2c = busio.I2C(board.SCL, board.SDA)
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Serial communication (sensor data)
sensor = adafruit_bno055.BNO055_I2C(i2c)  # IMU sensor

# Initialize variables for heading, distance, and control logic
heading = 0.0
roll = 0.0
pitch = 0.0
dis = 0.0
value = 360  # Default target heading is 360 degrees
count = 0
increment = False
logic = False
flag = True
time.sleep(3)  # Initial delay for sensor and system to stabilize

# Function to handle left-turn journey logic based on distance and heading
def L_journey(heading, dis, value, logic, flag, increment, count, init):
    # Initialization block for the first run
    if init:
        value = 360  # Reset target heading to 360 degrees
        count = 0
        increment = False
        logic = False
        flag = True
        init = False
        print("Initialized")

    # If the distance is >= 120 or the logic flag is True, execute the turn
    if (dis >= 120 or logic):
        # Adjust the target heading (value) by 90 degrees to the left (counterclockwise)
        if flag:
            value -= 90
            if value == 0:  # If the value is 0, reset it to 360
                value = 360
                increment = True  # Mark increment flag as True
            flag = False  # Disable the flag after making the adjustment

        # Check if the current heading is not within a certain range of the target value
        if (heading not in range(value - 60, value + 5)):
            print("turning", heading, value, dis)

            # Special case for transitioning near 0 degrees heading
            if heading <= 10 and value == 270:
                pi.set_servo_pulsewidth(18, 1100)  # Adjust drive motor to slow down
                pi.set_servo_pulsewidth(13, 1560)  # Adjust steering to turn left

            # Another special case when heading is near 360 and the target is 360
            elif value == 360 and heading <= 100:
                pi.set_servo_pulsewidth(18, max(1100, min(1900, 1500 + ((value - 360) - heading) * 18)))  # Turn drive motor
                pi.set_servo_pulsewidth(13, 1560)  # Turn steering
                print("Condition b")
            else:
                # General case for turning left
                pi.set_servo_pulsewidth(18, max(1100, min(1900, 1500 + (value - heading) * 18)))  # Adjust drive motor
                pi.set_servo_pulsewidth(13, 1560)  # Adjust steering

            logic = True  # Enable the logic flag
        else:
            # Once the robot is within the target heading range, move straight
            pi.set_servo_pulsewidth(18, 1600)  # Drive motor straight
            pi.set_servo_pulsewidth(13, 1560)  # Steering straight
            logic = False  # Disable the logic flag
            time.sleep(0.3)  # Delay to stabilize movement
    else:
        # If no turn is needed, maintain the current state
        flag = True  # Reset the flag
        if increment:
            count = count + 1  # Increment the turn count
            increment = False  # Disable the increment flag
        print(heading, dis, value)

        # Call the PID controller to maintain heading and move straight
        pi.set_servo_pulsewidth(18, pid(value, heading, 20))  # Adjust drive motor based on PID
        pi.set_servo_pulsewidth(13, 1560)  # Keep steering straight

    return value, logic, flag, increment, count

# Function to maintain the robot's movement in a straight line
def move(heading, value):
    pi.set_servo_pulsewidth(18, pid(value, heading, 20))  # Adjust drive motor based on PID
    pi.set_servo_pulsewidth(13, 1550)  # Keep steering straight
