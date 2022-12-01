# 0714.py

import cv2
import numpy as np

#1
# src = cv2.imread('./data/hand.jpg')
# src = cv2.imread('./data/lena.jpg')
src = cv2.imread('./data/car_num2.jpg')

src2 = cv2.imread('./data/flower.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

data = src.reshape((-1, 3)).astype(np.float32)
data2 = hsv.reshape((-1, 3)).astype(np.float32)

#2
K = 2                   #색상의 갯수
term_crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, labels, centers = cv2.kmeans(data, K, None, term_crit, 5, cv2.KMEANS_RANDOM_CENTERS)

print('centers.shape = ', centers.shape)
print('labels.shape = ', labels.shape)
print('ret = ', ret)



#2-2

L = 2
term_crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret2, labels2, centers2 = cv2.kmeans(data2, K, None, term_crit, 5, cv2.KMEANS_RANDOM_CENTERS)

print('centers2.shape = ', centers.shape)
print('labels2.shape = ', labels.shape)
print('ret2 = ', ret2)


#3
centers = np.uint8(centers)
res = centers[labels.flatten()]
dst = res.reshape(src.shape)

# labels2 = np.uint8(labels.reshape(src.shape[:2]))
# print('labels2.max() = ', labels2.max())
# dst = np.zeros(src.shape, dtype = src.dtype)
# for i in range(K):
#     r = np.random.randint(256)
#     g = np.random.randint(256)
#     b = np.random.randint(256)
#     dst[labels2 == i] = [b, g, r]

cv2.imshow('dst', dst)
# cv2.imshow('hsv', hsv)
# cv2.imshow('src', src)
# cv2.imshow('src2', src2)
# cv2.imshow('res', res)

cv2.waitKey()
cv2.destroyAllWindows()


