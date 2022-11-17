# 0402.py

import cv2

img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
print('img.shape=', img.shape)
print('img.shape[0]', img.shape[0])
print('img.shape[0]', img.shape[2])



img = img.flatten()
print('img.shape=', img.shape)

img = img.reshape(-1, 512, 512)
print('img.shape=', img.shape)

cv2.imshow('img', img[0])
cv2.waitKey()
cv2.destroyAllWindows()