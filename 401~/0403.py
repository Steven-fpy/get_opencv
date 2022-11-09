# 0403.py

import cv2
# import numpy as np

img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# img[100, 200] = 0               #화소값(밝기, 그레이스케일) 변경
img[500][500] = 0
print(img[100:110, 200:210])    #ROI(관심영역) 접근

##for y in range(100, 400):
##  for x in range(200, 300):
##      img[y, x] = 0

# img[100:400, 200:300] = 0       #ROI 접근
img[250:280, 250:350] = 0       #ROI 접근  시작점 : 끝점 y축 , 시작점 : 끝점 x축

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()