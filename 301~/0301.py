# 0301.py

import cv2
import numpy as np
#White 배경 생성

img = np.zeros(shape = (512, 512, 3), dtype = np.uint8) + 255
# img = np.ones((512, 512, 3), np.uint8) * 255
# img = np.full((512, 512, 3), (255, 255, 255),dtype = np.uint8)
# img = np.zeros((512, 512, 3), np.uint8)			#black 배경
pt1 = 100,100
pt2 = 400, 400
cv2.rectangle(img, pt1, pt2, (0,255 , 255), -1)

cv2.line(img, (200, 200), (500, 250), (255, 255, 0), 5)
cv2.line(img, (100, 400), (250, 500), (255, 0, 255), 5)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
