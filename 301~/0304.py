# 0304.py
import cv2
import numpy as np

img = np.zeros(shape = (512, 512, 3),dtype = np.uint8) + 255
ptCenter = img.shape[1] // 2, img.shape[0] // 2
size = 200,100
cy = img.shape[0] // 2
cx = img.shape[1] // 2

cv2.ellipse(img, ptCenter, size, 125, 0, 360, (0, 255, 0),3)
cv2.ellipse(img, ptCenter, size, 90, 0, 360, (0, 255, 255),3)
# cv2.circle(img, ptCenter, size, 45, 0, 360, (0, 0, 255),-1)

cv2.circle(img, (cx, cy), radius = 150, color = (255, 0, 255), thickness = 5)
cv2.circle(img, (cx, cy), radius = 120, color = (255, 0, 255), thickness = -1)
cv2.circle(img, (cx, cy), radius = 20, color = (255, 100, 0), thickness = -1)
cv2.circle(img, (cx, cy), radius = 30, color = (0, 0, 255), thickness = 2)
cv2.circle(img, (cx, cy), radius = 28, color = (0, 50, 255), thickness = 2)
cv2.circle(img, (cx, cy), radius = 26, color = (0, 50, 200), thickness = 2)
cv2.circle(img, (cx, cy), radius = 24, color = (0, 70, 200), thickness = 2)
cv2.circle(img, (cx, cy), radius = 22, color = (0, 0, 255), thickness = 2)

cv2.ellipse(img, ptCenter, size, 0, 0, 360, (255, 0, 0),5)
cv2.ellipse(img, ptCenter, size, 45, 0, 360, (0, 0, 255),5)

box = (ptCenter, size, 0)
cv2.ellipse(img, box, (255, 0, 0), 5)

box = (ptCenter, size, 90)
cv2.ellipse(img, box, (255, 0, 0), 10)

box = (ptCenter, size, 125)
cv2.ellipse(img, box, (255, 0, 0), 5)

box = (ptCenter, size, 45)
cv2.ellipse(img, box, (255, 0, 0), 10)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
