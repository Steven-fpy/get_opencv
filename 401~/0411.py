 # 0411.py
import cv2                          #cv2 를 불러옴
import numpy as np                  #numpy 불러옴

src = cv2.imread('./data/lena.jpg') #lena.jpg 파일을 로드
# img = cv2.imread('./data/lena.jpg')
# src = cv2.imread('./data/lena.jpg', cv2.IMREAD_COLOR)
# shape = src.shape[0], src.shape[1], 3
# dst = np.zeros(shape, dtype=np.uint8)
# dst2 = np.zeros(shape, dtype=np.uint8)
# dst3 = np.zeros(shape, dtype=np.uint8)



# print(type(dst))
# print(type(dst[0]))
b,g,r = cv2.split(src)          #b,g,r 을 선언하고 src를 cv2의 
                                #split을 사용하여 나눈다.
bMat = np.zeros((src.shape[0], src.shape[1],3), np.uint8)
# bMat = np.zeros((src.shape[0], src.shape[1],4), np.uint8)
# 결국 np.zeros((3, 3, 3), np.uint8의 구조라고 생각하면된다.
# 3x3 모양의 3차원 배열
# zeros는 0으로 가득찬 array를 생성한다.
# bMat를 선언하고 넘파이의 zeros안의 src에 담긴shape의 [0]번,[1]번 , 3개 채널

gMat = bMat.copy()      #gMat를 bMat의 내용으로 복사합니다.
rMat = bMat.copy()
lMat = bMat.copy()



bMat[ :, :, 0 ] = b     #bMat의 0번 채널인 blue채널을 b라고 지정한다.
gMat[ :, :, 1 ] = g     #gMat의 0번 채널인 green채널을 g라고 지정한다.
rMat[ :, :, 2 ] = r
# lMat[ :, :, 3 ] = l


# dst = [bMat,gMat,rMat]
# dst = [bMat,gMat,rMat,lMat]


# dst[0] = dst[ :, :, 0 ] = src 
# dst[1] = dst[ :, :, 1 ] = src
# dst[2] = dst[ :, :, 2 ] = src

# img[100:400, 200:300,0] = 255
# img[100:400, 200:300,1] = 255
# img[100:400, 200:300,2] = 255

# for i in range(0,3):
#     i = 0
#     i += i
# dst1[100:100, 200:300, :] = [255, 255, 255]
# dst2[100:100, 200:300, :] = [255, 255, 255]
# dst3[100:100, 200:300, :] = [255, 255, 255]


cv2.imshow('blue', bMat)
cv2.imshow('green', gMat)
cv2.imshow('red', rMat)     #'red'라는 창 이름의 rMat를 호출합니다.
# cv2.imshow('red2', lMat)

# cv2.imshow('green', img)
cv2.waitKey()               #key입력을 기다립니다.
cv2.destroyAllWindows()     #모든 창을 제거합니다.
