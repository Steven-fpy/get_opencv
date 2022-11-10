# 0406.py

import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg')                         #컬러
# img = cv2.imread('./data/lena.jpg')         # cv2.IMREAD_COLOR

# src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE) #흑백
# dst = np.zeros(src.shape, dtype = src.dtype)              #흑백
# dst = np.zeros(src.shape, src.dtype)                        #컬러
dst = src.copy()


# img[100, 200] = [255, 0, 0]                 # 컬러(BGR) 변경
# print(img[100, 200:210])                    # ROI 접근


# 오버헤드 : 필요이상의 부하를 주는 현상


# img[100:400, 200:300] = [0, 255, 0]         # ROI 접근
# img2 = src[250:280, 310:360].copy()
N = 84                                                     #모자이크 밀도
# height, width = src.shape                                 #흑백
# height, width, channel = src.shape                          #컬러
height, width = src.shape[0:2]


h = height // N
w = width // N

rect = [(200, 250), 0, 100]

startY = rect[0][0]         #200
startX = rect[0][1]         #200
endY = startY + rect[1]     #400
endX = startX + rect[2]     #400


for y in range(startY, endX, h):
    for x in range(startX, endX, w):
        roi = src[y:y + h, x:x + w]
        dst[y:y + h, x:x + w] = cv2.mean(roi)[0:3]




# for i in range(N):
#     for j in range(N):
        
#         y = min(startY + (i*h), endY)
#         x = min(startX + (j*w), endX)

        # x = startX + (j*w)


        # y = (h - 100) + h*i  #이것도 재밌다 격자
        # x = (j-100) * w  #이것도 재밌다 격자
        
        # y = ((i * h) + 200)+(i  - 200) #이것도 재밌다
        # x = ((j * w) + 200)+(j  - 200) #이것도 재밌다
                
        # y = ((i * h) + 200)+((i * h) - 200) #이것도 재밌다 격자
        # x = ((j * w) + 200)+((j * w) - 200) #이것도 재밌다 격자
        # y = i * h
        # x = j * w

        # roi = src[y:y + h, x:x + w]
        # dst[y:y + h, x:x + w] = cv2.mean(roi)[0]          #흑백
        # dst[y:y + h, x:x + w] = cv2.mean(roi)[0:3]          #컬러

cv2.imshow('dst', dst)
# cv2.imshow('dst', dst)

# cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()

