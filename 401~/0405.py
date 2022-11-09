# 0405.py

import cv2
##import numpy as np

img = cv2.imread('./data/lena.jpg')         # cv2.IMREAD_COLOR
# img[100, 200] = [255, 0, 0]                 # 컬러(BGR) 변경
# print(img[100, 200:210])                    # ROI 접근

##for y in range(100, 400):
##      for x in range(200, 300):
##          img[y, x] = [255, 0, 0]         # 파란색으로 변경

# img[250:280, 310:360] = [0, 255, 0]         # ROI 접근
img[100:400, 200:300, 0] = 255         # ROI 접근
img[100:400, 300:400, 1] = 255         # ROI 접근
img[100:400, 400:500, 2] = 255         # ROI 접근

# img2 = img[250:280, 310:360].copy()


cv2.imshow('img', img)
# cv2.imshow('img2', img2)

cv2.waitKey()
cv2.destroyAllWindows()