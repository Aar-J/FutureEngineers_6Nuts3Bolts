from picamera2 import Picamera2, Preview
import cv2
import numpy as np
import time
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="libpng")

# Create a Picamera2 instance
picam2 = Picamera2()

# Configure the camera for video
video_config = picam2.create_video_configuration(
    main={"size": (640, 480)},  # Reduce the resolution for higher frame rate
    controls={"FrameDurationLimits": (33333, 33333)}  # Set frame duration to approximately 30 fps
)

# Apply the configuration
picam2.configure(video_config)

# Start the camera
picam2.start()

# Allow some time for the camera to start
time.sleep(2)

# Define the range of the color you want to detect in HSV
# Example: Detecting a green object
lower_color = np.array([35, 100, 50])
upper_color = np.array([85, 255, 255])

while True:
    # Capture an image as a numpy array
    image = picam2.capture_array()
    
    # Convert the image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Create a binary mask where the color ranges are within the specified range
    mask = cv2.inRange(hsv, lower_color, upper_color)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw rectangle around the largest contour
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Convert the 2D mask to a 3-channel image
    mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    
    # Draw contours on a copy of the frame
    frame_contours = image.copy()
    cv2.drawContours(frame_contours, contours, -1, (0, 255, 0), 2)
    
    # Resize all frames to the same dimensions
    target_height, target_width = image.shape[:2]
    hsv_resized = cv2.resize(hsv, (target_width, target_height))
    mask_resized = cv2.resize(mask_rgb, (target_width, target_height))
    contours_resized = cv2.resize(frame_contours, (target_width, target_height))
    frame_resized = cv2.resize(image, (target_width, target_height))
    
    # Convert everything to 3 channels if they are not already
    if hsv_resized.shape[2] == 4:
        hsv_resized = cv2.cvtColor(hsv_resized, cv2.COLOR_RGBA2BGR)
    if frame_resized.shape[2] == 4:
        frame_resized = cv2.cvtColor(frame_resized, cv2.COLOR_RGBA2BGR)
    if contours_resized.shape[2] == 4:
        contours_resized = cv2.cvtColor(contours_resized, cv2.COLOR_RGBA2BGR)
    if mask_resized.shape[2] == 4:
        mask_resized = cv2.cvtColor(mask_resized, cv2.COLOR_RGBA2BGR)
    
    # Stack images to create a 2x2 grid
    top_row = np.hstack((hsv_resized, mask_resized))
    bottom_row = np.hstack((contours_resized, frame_resized))
    frame_composite = np.vstack((top_row, bottom_row))

    # Display the resulting frame
    cv2.imshow('Frame', frame_composite)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the OpenCV window
cv2.destroyAllWindows()

# Stop the camera
picam2.stop()

