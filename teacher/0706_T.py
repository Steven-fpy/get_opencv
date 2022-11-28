#0706.py
import cv2
import numpy as np
import time

#1
src = np.zeros((512,512,3), np.uint8)
cv2.rectangle(src, (50,100), (450,400), (255,255,255), -1)
cv2.rectangle(src, (100,150), (400,350), (0,0,0), -1)
cv2.rectangle(src, (200,200), (300,300), (255,255,255), -1)
cv2.rectangle(src, (240,240), (260,260), (0,0,0), -1)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)


#2
# mode = cv2.RETR_EXTERNAL
# mode = cv2.RETR_LIST
# mode = cv2.RETR_TREE
mode = cv2.RETR_CCOMP

method = cv2.CHAIN_APPROX_SIMPLE
# method = cv2.CHAIN_APPROX_NONE

contours, hierarchy = cv2.findContours(gray, mode, method)
print('type(contours)=', type(contours))
print('type(contours[0])=', type(contours[0]))
print('len(contours)=', len(contours))
print('countours[0].shape=', contours[0].shape)
print('countours[0]=', contours[0])
print('hierarchy=', hierarchy)

# hierarchy 계층
# 상관관계가 있는 인덱스 값, -1은 없음
# [Next, Previous, First Child, Parent]

# List
# [[
#   [ 1 -1 -1 -1]
#   [ 2  0 -1 -1]
#   [-1  1 -1 -1]
# ]]

# Tree
# [[
#    [-1 -1  1 -1]
#    [-1 -1  2  0]
#    [-1 -1 -1  1]
# ]]

# CCOMP
# [[
#    [ 1 -1 -1 -1]
#    [-1  0  2 -1]
#    [-1 -1 -1  1]
# ]]
# [[
#    [ 2 -1  1 -1]
#    [-1 -1 -1  0]
#    [-1  0  3 -1]
#    [-1 -1 -1  2]
# ]]


#3
cv2.drawContours(src, contours, -1, (255,0,0), 3)

#4
for contour in contours:
    # print('len(contour)=', len(contour))
    # print('contour=', contour)

    for pt in contour:
        cv2.circle(src, (pt[0][0], pt[0][1]), 5, (0,0,255), -1)
        # cv2.circle(src, (pt[0], pt[1]), 5, (0,0,255), -1)

    # pt = contour[0]
    # print('pt=', pt)


# for pt in contours[0][:]:
#     cv2.circle(src, (pt[0][0], pt[0][1]), 5, (0,0,255), -1)

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()

