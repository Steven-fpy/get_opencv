# 0716.py

import cv2
import numpy as np

#1
# src = cv2.imread('./data/circles.jpg')
src = cv2.imread('./data/car_num1.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, res = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

# cv2.imshow('res',res)

# def roid():
def detect():
        # cv2.imshow('img', dst)
        # cv2.waitKey()

    # cv2.destroyAllWindows()




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

    dst = src.copy()    # 추가한것
    #4
    # dst = img.copy()
    for i in range(1, int(ret)):
        x, y, width, height, area = stats[i]

        print('area = ', area)

        if area < 500 or area > 3500:
            continue

        # cv2.rectangle(dst, (x, y), (x + width, y + height), (0, 0, 255), 3)
        cv2.rectangle(dst, (x, y), (x + width, y + height), (255, 0, 255), 3)

        # cx, cy = centroids[i]
        # cv2.circle(dst, (int(cx), int(cy)), 5, (255, 0, 0), -1)

    cv2.imshow('dst', dst)
    roi = cv2.selectROI(dst)
    print('roi', roi)

    if roi != (0, 0, 0, 0):
        img = dst[roi[1]:roi[1] +roi[3],
                    roi[0]:roi[0] + roi[2]]

        cv2.imshow('img', img)
# roid()
detect()
# cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()
