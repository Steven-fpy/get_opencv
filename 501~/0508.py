#0508.py
import cv2
import numpy as np

#1
# src = cv2.imread('./data/Penguins.jpg')
src = cv2.imread('./data/fruits.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

#2
roi = cv2.selectROI(src)
print('roi =', roi)
roi_h = h[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]]
hist = cv2.calcHist([roi_h], [0], None, [64], [0,256])
backP = cv2.calcBackProject([h.astype(np.float32)], [0],
                            hist, [0, 256], scale = 1.0)



#3