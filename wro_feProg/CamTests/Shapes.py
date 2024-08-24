from picamera2 import Picamera2, Preview
import cv2

picam = Picamera2()
config = picam.create_video_configuration(main = {"size" : (640,480)},
                                          controls = {"FrameDurationLimits": (33333,33333)})

picam.configure(config)
picam.start()

while True:
    img = picam.capture_array()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    for i in range(120):
        img[120+i:(121+i),(0):(120-i),:] = 0
        img[120+i:(121+i),(520+i):(640),:] = 0
    img[0:120,(0):640,:] = 0
    cv2.imshow("Camera", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
picam.stop()
cv2.destroyAllWindows()
