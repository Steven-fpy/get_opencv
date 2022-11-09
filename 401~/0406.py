# 0406.py

import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg')                         #컬러
# src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE) #흑백
# dst = np.zeros(src.shape, dtype = src.dtype)              #흑백
dst = np.zeros(src.shape, src.dtype)                        #컬러

N = 84                                                      #모자이크 밀도
# height, width = src.shape                                 #흑백
height, width, channel = src.shape                          #컬러

h = height // N
w = width // N
for i in range(N):
    for j in range(N):
        y = i * h
        x = j * w
        roi = src[y:y + h, x:x + w]
        # dst[y:y + h, x:x + w] = cv2.mean(roi)[0]          #흑백
        dst[y:y + h, x:x + w] = cv2.mean(roi)[0:3]          #컬러

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

