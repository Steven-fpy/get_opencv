# 0409.py

import cv2
src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

dst = src.copy()
dst[100:400, 200:300] = 200 

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
