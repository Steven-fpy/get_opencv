# # # import numpy as np
import cv2
import sys
# # from matplotlib import pyplot as plt 

# src = cv2.imread('./data/ind.jpg')
# src3 = cv2.imread('./data/ind.jpg',cv2.IMREAD_GRAYSCALE)

# dst = src.copy()
# dst2 = src.copy()
# hsv = cv2.cvtColor(dst,cv2.COLOR_BGR2HSV)
# hsv2 = cv2.cvtColor(dst2,cv2.COLOR_BGR2HSV)


# ret, mask2 = cv2.threshold(hsv, 100, 255, cv2.THRESH_BINARY) 
# ret2, mask4 = cv2.threshold(hsv2, 100, 255, cv2.THRESH_BINARY_INV) 

# mask = cv2.inRange(hsv, (-30,-30,100), (130,255,255)) 
# mask3 = cv2.inRange(hsv2, (-30,-30,100), (130,255,255)) 

# rows,cols,channels = dst.shape

# roi = src[0:rows, 0:cols]

# dst = cv2.copyTo(src, mask = mask)
# hsv = cv2.cvtColor(dst,cv2.COLOR_BGR2HSV)



# # src1 = cv2.bitwise_or(mask2,mask)
# # cv2.imshow('src1_bg',src1)
# cv2.imshow('src3', src3)
# # # # 이미지를 불러온다.






# # fig,ax = plt.subplots(figsize=(7,7))

# # a=ax.grid()

# # # ax.grid(axis = 'x',
# # #         linewidth = 5)
# cv2.imshow('mask', mask)
# cv2.imshow('mask2', mask2)
# cv2.imshow('mask3', mask3)
# cv2.imshow('mask4', mask4)


# # cv2.imshow('src', src)
# # cv2.imshow('src', hsv)
# cv2.waitKey()
# cv2.destroyAllWindows()



# # cv2.imshow('src', src)
# # cv2.waitKey()
# # cv2.destroyAllWindows()








src = cv2.imread('./data/ind.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

dst1 = cv2.inRange(src, (0, 50, 200), (50, 100, 255))
dst2 = cv2.inRange(src_hsv, (-30, 30, 100), (50, 150, 255))
dst3 = cv2.bitwise_or(dst1, dst2)
# print('dst1 : ', dst1)
# print('dst2 : ', dst2)
# print('dst3 : ', dst3)


# src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV) # BGR -> HSV 로 변경(색상 검출에 효율적)

# # 트랙바 콜백 함수 생성
# def on_trackbar(pos):
#     hmin = cv2.getTrackbarPos('H_min', 'dst') # 트랙바의 위치를 받아옴 (h_min 값)
#     hmax = cv2.getTrackbarPos('H_max', 'dst')
    
#     dst = cv2.inRange(src_hsv, (hmin, 150, 0), (hmax, 255, 255))
#     cv2.imshow('dst', dst)
    
# cv2.imshow('src', src)
# cv2.namedWindow('dst')

# # 트랙바 콜백 함수 등록
# cv2.createTrackbar('H_min', 'dst', 50, 179, on_trackbar)
# cv2.createTrackbar('H_max', 'dst', 80, 179, on_trackbar)
# on_trackbar(0)

cv2.imshow('src', src)
# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)

cv2.waitKey()

cv2.destroyAllWindows()