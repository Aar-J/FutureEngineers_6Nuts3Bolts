import numpy as np
import cv2
from picamera2 import Picamera2
from time import sleep

# Known parameters
KNOWN_WIDTH = 4.9  # Known width of the object in cm
FOCAL_LENGTH = 968.75  # 2.75mm Example focal length, you need to calibrate your camera to find this

def find_distance(width_in_image):
    return (KNOWN_WIDTH * FOCAL_LENGTH) / width_in_image

picamera2 = Picamera2()
config = picamera2.create_video_configuration(main={"size": (640, 480)})
picamera2.configure(config)

picamera2.start()
while True:
    image = picamera2.capture_array()
    image = cv2.flip(image, -1)
    imagergb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imagehsv = cv2.cvtColor(imagergb, cv2.COLOR_BGR2HSV)
    key = cv2.waitKey(1)
    
    # Define range for green color
    lower_green = np.array([35, 100, 50])
    upper_green = np.array([80, 255, 255])
    
    # Define range for red color
    lower_red1 = np.array([0, 100, 50])
    upper_red1 = np.array([15,255, 255])
    lower_red2 = np.array([170, 100, 50])
    upper_red2 = np.array([180, 255, 255])
    
    # Create masks for green and red colors
    mask_green = cv2.inRange(imagehsv, lower_green, upper_green)
    mask_red1 = cv2.inRange(imagehsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(imagehsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    
    # Find contours for green mask
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw rectangles around detected green contours
    for contour in contours_green:
        area = cv2.contourArea(contour)
        if area > 1200:  # Adjust the threshold as needed
            x, y, w, h = cv2.boundingRect(contour)
            distance = find_distance(w)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, f'Area: {int(area)}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(image, f'Green', (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(image, f'Distance: {distance:.2f} cm', (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Find contours for red mask
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw rectangles around detected red contours
    for contour in contours_red:
        area = cv2.contourArea(contour)
        if area > 1200:  # Adjust the threshold as needed
            x, y, w, h = cv2.boundingRect(contour)
            distance = find_distance(w)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(image, f'Area: {int(area)}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.putText(image, f'Red', (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.putText(image, f'Distance: {distance:.2f} cm', (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the image with contours and areas
    cv2.imshow("image_combined", image)
    
    if key == ord("q") or key == 27:
        break

picamera2.stop()
cv2.destroyAllWindows()
