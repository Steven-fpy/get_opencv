# 0720_ex.py

import cv2
import numpy as np

src = cv2.imread('./data/car_num2.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, res = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

ret, labels, stats, centroids = cv2.connectedComponentsWithStats(res)
print('ret = ', ret)
print('stats = ', stats)
print('centroids = ', centroids)

dst = np.zeros(src.shape, dtype = src.dtype)
for i in range(1, int(ret)):
    r = np.random.randint(256)
    g = np.random.randint(256)
    b = np.random.randint(256)
    dst[labels == i ] = [b, g, r]

for i in range(1, int(ret)):
    x, y, width, height, area = stats[i]
    cv2.rectangle(dst, (x, y), (x + width, y + height), (0, 0, 255), 2)

    cx, cy = centroids[i]
    cv2.circle(dst, (int(cx), int(cy)), 5, (255, 0, 0), -1)

cv2.imshow('src', src)


cv2.imshow('dst',dst)

cv2.imshow('res',res)
cv2.waitKey()
cv2.destroyAllWindows()
