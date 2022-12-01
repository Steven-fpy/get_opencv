# 0705.py

import cv2
import numpy as np


#이걸 일단 그레이스케일로 바꾸고 시도해보자

#1
# src1 = cv2.imread('./data/hand.jpg')
src1 = cv2.imread('./data/car_num1.jpg',cv2.IMREAD_GRAYSCALE)
hsv1 = cv2.cvtColor(src1, cv2.COLOR_BGR2HSV)
# lowerb1 = (0, 40, 0)
# upperb1 = (20, 180, 255)

lowerb1 = (0, 0, 0)

upperb1 = (10, 15, 100)
dst1 = cv2.inRange(hsv1, lowerb1, upperb1)

# hsv = h 색상 s 채도 v 명도


#2
# src1 = cv2.imread('./data/flower.jpg')
src2 = cv2.imread('./data/car_num2.jpg')
hsv2 = cv2.cvtColor(src2, cv2.COLOR_BGR2HSV)
# lowerb2 = (150, 100, 150)
# upperb2 = (180, 255, 255)
lowerb2 = (0, 0, 0)
upperb2 = (5, 50, 100)

dst2 = cv2.inRange(hsv2, lowerb2, upperb2)

#3
cv2.imshow('src1', src1)
cv2.imshow('dst1', dst1)
cv2.imshow('src2', src2)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()
