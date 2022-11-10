# 0411.py
import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg') #bgr

# cv2.imshow('blue', dst[0])
# cv2.imshow('green', dst[1])
# cv2.imshow('red', dst[2])

bMat = np.zeros((src.shape[0], src.shape[1], 3), np.uint8)
gMat = bMat.copy()
rMat = bMat.copy()

# dst = cv2.split(src)
# bMat[:,:,0] = dst[0] #b
# gMat[:,:,1] = dst[1] #g
# rMat[:,:,2] = dst[2] #r

b,g,r = cv2.split(src)
bMat[:,:,0] = b #b
gMat[:,:,1] = g #g
rMat[:,:,2] = r #r

cv2.imshow('blue', bMat)
cv2.imshow('green', gMat)
cv2.imshow('red', rMat)

cv2.waitKey()
cv2.destroyAllWindows()