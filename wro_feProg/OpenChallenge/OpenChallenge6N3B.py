import time
import board
import busio
import adafruit_bno055
import sys
import serial
sys.path.append('/usr/lib/python3/dist-packages')  # Add the system path for python packages
BUTTON_PIN = 17  # Define the GPIO pin for the button input
import pigpio
from picamera2 import Picamera2, Preview  # Camera control for preview
import cv2

import JourneyLeft as l  # Import the custom JourneyLeft module
import JourneyRight as r  # Import the custom JourneyRight module

# Initialize pigpio instance
pi = pigpio.pi()

# Set GPIO modes
pi.set_mode(18, pigpio.OUTPUT)  # Set GPIO pin 18 for drive motor control
pi.set_mode(13, pigpio.OUTPUT)  # Set GPIO pin 13 for steering servo control
pi.set_mode(BUTTON_PIN, pigpio.INPUT)  # Set GPIO pin 17 for button input
pi.set_pull_up_down(BUTTON_PIN, pigpio.PUD_UP)  # Enable pull-up resistor on button pin

# Initialize I2C and serial communication
i2c = busio.I2C(board.SCL, board.SDA)  # Initialize I2C for BNO055 sensor
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Open serial communication on USB port for sensor data
sensor = adafruit_bno055.BNO055_I2C(i2c)  # Initialize BNO055 sensor over I2C

# Initialize variables
heading = 0.0  # Robot's heading angle from the sensor
dis = 0.0  # Distance traveled by left side
value = 360  # Initial target value (angle or motor power control)
count = 0  # Counter for the number of completed actions or maneuvers
increment = False  # Flag for incrementing maneuvers
logic = False  # Logic flag for controlling behavior
flag = True  # General-purpose flag
init = True  # Flag to control initialization of journeys
left = 0  # Indicates direction of travel, 1 for left, 2 for right

# Read the first sensor data from the serial port (distance information)
data = ((ser.readline().decode('utf-8', errors='ignore').rstrip()))  # Read distance data
try:
    dis, distanceRight = map(float, data.split(','))  # Parse left and right distances
except:
    dis = distanceRight = 0  # Handle cases where data is invalid
print(dis, distanceRight)  # Print distance data for debugging
time.sleep(3)  # Short delay before starting the main loop

# Wait for the button press to start the main loop
try:
    while pi.read(BUTTON_PIN) == 1:  # Wait for the button to be pressed
        time.sleep(0.1)  # Polling delay
except KeyboardInterrupt:
    print("Program Interrupted")
    exit()  # Exit if interrupted by keyboard

# Main control loop for running the robot's journeys
while count < 3:  # Loop runs for 3 journey iterations
    heading, _, __ = sensor.euler  # Read Euler angles (heading, pitch, roll) from the BNO055 sensor
    try:
        heading = min(360, max(0, heading))  # Clamp heading between 0 and 360 degrees
    except:
        heading = 0  # Set heading to 0 if sensor data is invalid
    
    # Read distance data again from the serial port
    data = ((ser.readline().decode('utf-8', errors='ignore').rstrip()))
    try:
        dis, distanceRight = map(float, data.split(','))  # Parse left and right distances
    except:
        dis = distanceRight = 0  # Handle invalid distance data

    # Control logic to determine which journey to run based on distance and direction
    if left == 1:  # If traveling left
        value, logic, flag, increment, count = l.L_journey(heading, dis, value, logic, flag, increment, count, init)
        left = 1  # Set left direction flag
        init = False  # Initialization completed
        print("LeftRunning")
    elif left == 2:  # If traveling right
        value, logic, flag, increment, count = r.R_journey(heading, distanceRight, value, logic, flag, increment, count, init)
        left = 2  # Set right direction flag
        print("RRunning")
        init = False  # Initialization completed
    elif (dis > distanceRight and dis > 100):  # If the left side has traveled farther
        value, logic, flag, increment, count = l.L_journey(heading, dis, value, logic, flag, increment, count, init)
        left = 1  # Set left direction flag
        init = False  # Initialization completed
        print("LeftRunning")
    elif (dis < distanceRight and distanceRight > 100):  # If the right side has traveled farther
        value, logic, flag, increment, count = r.R_journey(heading, distanceRight, value, logic, flag, increment, count, init)
        left = 2  # Set right direction flag
        print("RRunnnning")
        init = False  # Initialization completed
    else:
        l.move(heading, value)  # Move forward without changing direction
        print("NormalMove")
    
    # Check for 'q' or 'Q' key press to quit the program
    key = cv2.waitKey(1)
    if key == ord('Q') or key == ord('q'):
        break

# Final movement before exiting
l.move(heading, value)
time.sleep(0.1)

# Stop the steering servo by setting the pulse width to 0
pi.set_servo_pulsewidth(13, 0)
