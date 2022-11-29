#0708.py

import cv2
import numpy as np

#1
src = np.full((512, 512, 3), (255, 255, 255), dtype = np.uint8)
# 흰색의 빈공간 생성
cv2.rectangle(src, (50, 50), (200, 200), (0, 0, 255), 2)
# 빨강 네모생성
cv2.circle(src, (300, 300), 100, (0, 0, 255), 2)
# 붉은 원 생성

#2
dst = src.copy()
cv2.floodFill(dst, mask = None, seedPoint = (100, 100), newVal = (255, 0, 0))

# seedPoint -> 색상 칠할 시작점 지정, 지정위치부터 경계면까지 퍼져가면서 색을 채움

#3
retval, dst2, mask, rect = cv2.floodFill(dst, mask = None,
                                        seedPoint = (300, 300),
                                        newVal = (0, 255, 0))

print('rect', rect)
x, y, width, height = rect
cv2.rectangle(dst2, (x, y), (x + width, y + height), (255, 0, 0), 2)
# cv2.floodFill(dst, mask = None, seedPoint = (100, 100), newVal = (255, 0, 0))


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)

# cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()

