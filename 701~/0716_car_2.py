# 0716.py

import cv2
import numpy as np

#1
# src = cv2.imread('./data/circles.jpg')
# src = cv2.imread('./data/car_num2.jpg')
src = cv2.imread('./data/lena.jpg')

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, res = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('ret',ret)
res2 = res[200:300, 30: 480]
cv2.imshow('res',res)
cv2.imshow('res2',res2)


#pyramid

# down2 = cv2.pyrDown(src)
# down4 = cv2.pyrDown(down2)
# print('down2.shape=', down2.shape)
# print('down4.shape=', down4.shape)

# up2 = cv2.pyrUp(src)
# up4 = cv2.pyrUp(up2)
# print('up2.shape=', up2.shape)
# print('up4.shape=', up4.shape)

# cv2.imshow('down2', down2)
# cv2.imshow('down4', down4)
# cv2.imshow('up2', up2)
# cv2.imshow('up4', up4)

#resize
# rez = cv2.resize(dst,[480, 480])


#2
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(res)
print('ret = ', ret)
print('stats = ', stats)
print('centroids = ', centroids)

#3
# dst = np.zeros(src.shape, dtype = src.dtype)
# for i in range(1, int(ret)):
#     r = np.random.randint(256)
#     g = np.random.randint(256)
#     b = np.random.randint(256)
#     dst[labels == i ] = [b, g, r]

#4
dst = src.copy()
for i in range(1, int(ret)):
    x, y, width, height, area = stats[i]

    print('area = ', area)
    # if (area == 567):

    if (area < 300 or area > 566) and (area < 706 or area > 3460) :
        continue

    cv2.rectangle(dst, (x, y), (x + width, y + height), (0, 0, 255), 2)

    # cx, cy = centroids[i]
    # cv2.circle(dst, (int(cx), int(cy)), 5, (255, 0, 0), -1)
rez = dst[200:300, 30:480]

cv2.imshow('rez', rez)
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
