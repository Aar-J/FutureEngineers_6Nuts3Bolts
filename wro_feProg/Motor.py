import cv2
import numpy as np
from time import sleep
a = np.zeros([320,480])
cv2.imshow("frame",a)
sleep(1000)
cv2.destroyAllWindows()