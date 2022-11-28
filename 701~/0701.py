# 0701.py

import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

edges1 = cv2.Canny(src, 50, 10)
edges2 = cv2.Canny(src, 50, 200)
edges3 = cv2.Canny(src, 50, 400)
edges4 = cv2.Canny(src, 50, 800)
# edges5 = cv2.Canny(src, 50, 1000)


cv2.imshow('edges1', edges1)
cv2.imshow('edges2', edges2)
cv2.imshow('edges3', edges3)
cv2.imshow('edges4', edges4)
# cv2.imshow('edges5', edges5)

cv2.waitKey()
cv2.destroyAllWindows()

