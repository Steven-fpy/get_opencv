# 0707.py

import cv2
import numpy as np

#1
src = np.zeros(shape = (512, 512, 3), dtype = np.uint8)
# src = cv2.imread('./data/lena.jpg')
cv2.rectangle(src,(50, 100), (450, 400), (255, 255, 255), -1)
cv2.rectangle(src,(100, 150), (400, 350), (0, 0, 0), -1)
cv2.rectangle(src,(200, 200), (300,300), (255, 255, 255), -1)
cv2.rectangle(src,(240, 240), (260,260), (0, 0, 0), -1)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

#2
mode = cv2.RETR_LIST
method = cv2.CHAIN_APPROX_SIMPLE
# method = cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(gray, mode, method)
# cv2.drawContours(src, contours, -1, (255, 0, 0,), 3)  #모든 윤곽선

# print('type(contours) = ', type(contours))
# print('type(contours[0]) = ', type(contours[0]))
print('len(contours) = ', len(contours))
print('contours[0].shape = ', contours[0].shape)
print('contours = ', contours)
print('hierarchy = ', hierarchy)


#3
# cv2.drawFrameAxes(src, contours, -1, (255, 0, 0,), 3)  #모든 윤곽선
for cnt in contours:
    cv2.drawContours(src, [cnt], 0, (255, 0, 0), 3)

    for pt in cnt:      #윤곽선 좌표]
        cv2.circle(src, (pt[0][0], pt[0][1]),5 , (0, 0, 255), -1)

# for pt in contours[0][:]:       #윤곽선 좌표
#     cv2.circle(src, (pt[0][0], pt[0][1]),5 , (0, 0, 255), -1)

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()


#동생, 형, 첫째자식, 부모
#next, previous, first child, parent
# hierarchy =  
# [[
#   [ 1 -1 -1 -1]
#   [ 2  0 -1 -1]
#   [ 3  1 -1 -1]
#   [-1  2 -1 -1]
# ]]