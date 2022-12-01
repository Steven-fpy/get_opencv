# 0711.py

import cv2
import numpy as np

#1
# src = cv2.imread('./data/circles2.jpg')
src = cv2.imread('./data/car_num2.jpg')

# src = cv2.imread('./data/flower.jpg')

# 거리계산식이 포함된 주소
# L1, L2, LC
# https://076923.github.io/posts/C-opencv-44/

# 빛을 고르게 펴준다.
# merge camera 사용권장

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, bImage = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
dist = cv2.distanceTransform(bImage, cv2.DIST_L1, 3)
dist8 = cv2.normalize(dist, None, 0, 255, cv2.NORM_MINMAX, dtype = cv2.CV_8U)

cv2.imshow('bImage', bImage)
cv2.imshow('dist8', dist8)

#2
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(dist)
(dist > maxVal * 0.5)       # 0.5는 50%를 뜻하는데, 물이 최대한으로 차있는 상태에서 물을 부으면 넘치므로
                            # 100퍼센트는 사용안됨

print('dist: ', minVal, maxVal, minLoc, maxLoc)
# mask = (dist > maxVal * 0.5).astype(np.uint8) * 255   #이진화, threshold

print('test: ', dist > maxVal*0.5)


mask = np.zeros(dist.shape[:2], np.uint8)
mask[dist > maxVal * 0.5] = 255

np.ones

# dist 내의 원소가 maxVal*0.5 보다 크면 True 아니면 False 구성된 행렬을 반환하고
# 해당 행렬을 astype(np.uint8)로 변환시 ture는 1로 False는 0으로 구성된 행렬
# 해당 행렬에 *255 를 하면 0과 1로 구성된 원소들에 모두 255를 곱한 행렬을 반환한다



for y, cols in enumerate(dist):
    for x, col in enumerate(cols):
        if col > maxVal * 0.5:
            mask[y, x] = 255

cv2.imshow('mask', mask)

#3

mode =cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv2.findContours(mask, mode, method)
print('len(countours)= ', len(contours))

markers = np.zeros(shape = src.shape[:2], dtype = np.int32)
for i, cnt in enumerate(contours):
    cv2.drawContours(markers, [cnt], 0, i + 1, -1)

#4
dst = src.copy()
cv2.watershed(src, markers)

dst[markers == -1] = [0, 0, 255]    #경계선
for i in range(len(contours)):      #분할영역
    r = np.random.randint(256)
    g = np.random.randint(256)
    b = np.random.randint(256)
    dst[markers == i + 1] = [b, g, r]

dst = cv2.addWeighted(src, 0.4, dst, 0.6, 0)    #합성
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()