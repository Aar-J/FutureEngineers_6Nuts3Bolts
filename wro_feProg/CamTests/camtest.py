from picamera2 import Picamera2
from time import sleep
import cv2

picamera2 = Picamera2()
config = picamera2.create_video_configuration(main ={"size":(640,480)})
picamera2.configure(config)


picamera2.start()
while True:
    image=picamera2.capture_array()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    image = cv2.flip(image,-1)
    key = cv2.waitKey(1)
    cv2.imshow("image", image)
    if key == ord("q") or key == 27:
        break;
picamera2.stop()

cv2.destroyAllWindows()