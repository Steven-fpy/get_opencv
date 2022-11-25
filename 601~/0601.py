#0601.py
import cv2
import numpy as np

src = cv2.imread ('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.boxFilter(src, ddepth = -1, ksize = (11, 11))
dst2 = cv2.boxFilter(src, ddepth = -1, ksize = (21, 21))
dst2_1 = cv2.boxFilter(src, ddepth = -1, ksize = (31, 31))
dst2_2 = cv2.boxFilter(src, ddepth = -1, ksize = (41, 41))
dst2_3 = cv2.boxFilter(src, ddepth = -1, ksize = (51, 51))

dst3 = cv2.bilateralFilter(src, d = 1111, sigmaColor = 10, sigmaSpace = 10)

dst4 = cv2.bilateralFilter(src, d = -1, sigmaColor = 10, sigmaSpace = 10)

cv2.imshow('src', src)
cv2.imshow('dst', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst2_1', dst2_1)
cv2.imshow('dst2_2', dst2_2)
cv2.imshow('dst2_2', dst2_3)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)
cv2.waitKey()
cv2.destroyAllWindows()




