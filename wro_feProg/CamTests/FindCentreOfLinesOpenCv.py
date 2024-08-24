#Finding the center between the 2 black lanes 

import numpy as np
import cv2
from picamera2 import Picamera2
from time import sleep

# Initialize the camera
picamera2 = Picamera2()
config = picamera2.create_video_configuration(main={"size": (640, 480)})
picamera2.configure(config)

# Start the camera
picamera2.start()

while True:
    # Capture image from camera
    image = picamera2.capture_array()
    # Flip the image if necessary
    image = cv2.flip(image, -1)
    
    rgba = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #rgba[0: 240, 0:640, :] = 0 -> This is for slicing the frame so half of the frame turns black
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(rgba, cv2.COLOR_RGB2GRAY)
    
    # Apply binary thresholding
    _, binary_image = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY_INV)

    # Apply Canny edge detection on the binary image
    canny_image = cv2.Canny(binary_image, 100, 200)
    
    # Apply Hough Line Transform on the Canny edge-detected image
    lines = cv2.HoughLinesP(canny_image, 1, np.pi / 180, threshold=100, minLineLength=10, maxLineGap=100)
    
    lane_centers = []

    # Draw lines on the original image
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(rgba, (x1, y1), (x2, y2), (0, 255, 0), 4)
            # Calculate the midpoint of each detected line (representing the center of each lane)
            lane_center_x = (x1 + x2) // 2
            lane_center_y = (y1 + y2) // 2
            lane_centers.append((lane_center_x, lane_center_y))
    
    # Find the midpoint between the two lanes
    if len(lane_centers) >= 2:
        # Sort by x-coordinates to find the two lanes that are most likely to be the left and right lanes
        lane_centers = sorted(lane_centers, key=lambda point: point[0])
        left_lane_center = lane_centers[0]
        right_lane_center = lane_centers[-1]

        # Calculate the midpoint between the two lanes
        center_x = (left_lane_center[0] + right_lane_center[0]) // 2
        center_y = (left_lane_center[1] + right_lane_center[1]) // 2

        # Draw the center point as a red circle
        cv2.circle(rgba, (center_x, center_y), 5, (0, 0, 255), -1)
    
    # Convert Canny image to BGR so it can be stacked with the original
    canny_bgr = cv2.cvtColor(canny_image, cv2.COLOR_GRAY2BGR)

    # Display the original and Canny images side by side
    combined_image = np.hstack((rgba, canny_bgr))
    cv2.imshow("Original and Canny Image", combined_image)

    # Exit on 'q' or ESC key press
    key = cv2.waitKey(1)
    if key == ord("q") or key == 27:
        break

# Stop the camera and close windows
picamera2.stop()
cv2.destroyAllWindows()
