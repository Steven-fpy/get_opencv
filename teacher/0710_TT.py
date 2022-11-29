#0709.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

#1
src = cv2.VideoCapture(0)
# src = cv2.imread('./data/hand.jpg')
mask = np.zeros(shape=src.shape[:2], dtype=np.uint8)
markers = np.zeros(shape=src.shape[:2], dtype=np.int32)

dst = src.copy()
cv2.imshow('dst', dst)

#2
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(param[0], (x,y), 10, (255,255,255), -1)
            cv2.circle(param[1], (x,y), 10, (255,255,255), -1)

    cv2.imshow('dst', param[1])

#3
mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE


while True:
    cv2.setMouseCallback('dst', onMouse, [mask, dst])
    key = cv2.waitKey(30)

    if key == 0x1B:  #esc, 27
        break

    elif key == ord('r'):
        mask[:,:] = 0
        dst = src.copy()
        cv2.imshow('dst', dst)

    elif key == ord(' '):

        constours, hierarchy = cv2.findContours(mask, mode, method)
        print('len(contours)=', len(constours))
        markers[:,:] = 0 #초기화

        for i, cnt in enumerate(constours):
            cv2.drawContours(markers, [cnt], 0, i+1, -1)

        # markerM = markers.astype(np.uint8)
        # minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(markerM)
        # print('markerM: ', minVal, maxVal, minLoc, maxLoc)

        # ret, markerM = cv2.threshold(markerM, 0, 255, cv2.THRESH_BINARY)
        # cv2.imshow('markerM', markerM)

        # 그레이스케일 이미지에서 높은 픽셀값을 가지는 부분을 언덕으로 보고, 
        # 낮은 픽셀값을 가지는 부분을 계곡으로 볼 수 있습니다. 
        # 한 이미지에 여러 개의 고립된 계곡(극소점)이 있을 수 있습니다. 
        # 각각 다른 색의 물(라벨)로 물을 채운다고  합시다. 
        cv2.watershed(src, markers) 

        dst = src.copy()
        dst[markers == -1] = [0,0,255]  #경계선

        # for y, row in enumerate(markers):
        #     for x, v in enumerate(row):
        #          if v == -1:
        #             dst[y, x] = [0,0,255]

        for i in range(len(constours)): #분할영역
            r = np.random.randint(256)
            g = np.random.randint(256)
            b = np.random.randint(256)
            dst[markers == i+1] = [b,g,r]

            # for y, row in enumerate(markers):
            #     for x, v in enumerate(row):
            #          if v == i+1:
            #             dst[y, x] = [0,0,255]

    

        # dst = cv2.addWeighted(src, 0.4, dst, 0.6, 0)  #합성
        cv2.imshow('dst', dst)


cv2.destroyAllWindows()