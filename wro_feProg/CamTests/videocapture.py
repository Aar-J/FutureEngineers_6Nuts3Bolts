from picamera2 import Picamera2
from time import sleep
import cv2

picamera2 = Picamera2()
config = picamera2.create_video_configuration()
picamera2.configure(config)

video_writer = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"XVID"), 20.0, (640,480))

picamera2.start()
while True:
    image=picamera2.capture_array()
    video_writer.write(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    key = cv2.waitKey(1)
    cv2.imshow("image", image)
    if key == ord("q") or key == 27:
        break;

picamera2.stop()
video_writer.release()

cv2.destroyAllWindows()
