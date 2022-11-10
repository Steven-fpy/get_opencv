 # 0411.py
import cv2
import numpy as np

# src = cv2.imread('./data/lena.jpg')
# src2 = cv2.imread('./data/lena.jpg')
# src3 = cv2.imread('./data/lena.jpg')

# src2 = cv2.imread('./data/lena.jpg')
# src3 = cv2.imread('./data/lena.jpg')

src = cv2.imread('./data/lena.jpg')
# src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
shape = src.shape[0], src.shape[1], 3
# shape = src2.shape[0], src2.shape[1], 3
# shape = src3.shape[0], src3.shape[1], 3

dst = np.zeros(shape, dtype=np.uint8)
# dst2 = np.zeros(shape, dtype=np.uint8)
# dst3 = np.zeros(shape, dtype=np.uint8)
# cv2.imshow('dst',dst)
# cv2.imshow('src',src)

# cv2.waitKey()
# cv2.destroyAllWindows()

dst = cv2.split(src)
# print(type(dst))
# print(type(dst[0]))

# dst[ :, :, 0 ][ :, :, 1 ][ :, :, 2 ]= [255,255,255]
dst[ :, :, 1 ] = src
# dst[ :, :, 2 ] = src


# dst[ :, :, 0 ] = src1
# dst[ :, :, 1 ] = src2
# dst[ :, :, 2 ] = src3

# img[100:400, 200:300,0] = 255
# img[100:400, 200:300,1] = 255
# img[100:400, 200:300,2] = 255

# for i in range(0,3):
#     i = 0
#     i += i
dst[100:400, 200:300, :] = [255, 255, 255]

# dst[100:100, 200:300, :] = [255, 255, 255] = src1
# dst[100:100, 200:300, :] = [255, 255, 255] = src2
# dst[100:100, 200:300, :] = [255, 255, 255] = src3


# cv2.imshow('blue', dst[0])
# cv2.imshow('green', dst[1])
# cv2.imshow('red', dst[2])
cv2.imshow('green', src)
cv2.imshow('green', dst)
cv2.waitKey()
cv2.destroyAllWindows()
