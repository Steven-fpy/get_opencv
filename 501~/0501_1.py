#0501,py

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    retval, frame = cap.read()
    if not retval:
        break

    dst = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, dst = cv2.threshold(dst, 200, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    cv2.imshow('frame', frame)
    cv2.imshow('dst', dst)


# src = cv2.imread('./data/Heart10.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('src',src)
# 
# ret,dst = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY)
# print('ret = ', ret)            #ret = retval
# cv2.imshow('dst',dst)
# 
# ret2, dst2 = cv2.threshold(src, 200, 255,
                    # cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# print('ret2', ret2)
# cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()