#0212-2.py

import cv2
import time

class Animator():

    def __init__(self, initFunc, updateFrameFunc, interval):
        self.__initFunc = initFunc
        self.__updateFrameFunc = updateFrameFunc
        self.__interval = interval

    def show(self):
        # self.__initFunc.isOpened()
        self.__initFunc()
        # print('self._initFunc',a)
        # initFunc = initFunc
        # updateFrameFunc = updateFrameFunc
        # interval = interval
        # print('self.__updateFrameFunc', b)
              
        while True:
            self.__updateFrameFunc()
            pass
        pass
    
def init():
    retval, frame = cap.read()
    cv2.imshow('video', frame)

def updateFrame(k):
    # print('updateFrame: k: ', k)
    retval, frame = cap.read()
    if retval:
        cv2.imshow('video', frame)


cap = cv2.VideoCapture('./data/vtest.avi')
retval, frame = cap.read()
cv2.imshow('video', frame)

# 콜백함수를 연결
# ani = Animator(init, updateFrame, 50)
ani = Animator('./data/vtest.avi')

# a= 50
# a

# Animator()
#__init__은 클래스가 생성(호출)될 때 호출된다.

# show, 재생시작
ani.show()

if cap.isOpened():
    cap.release()
    #     # 처음으로 초기화 함수를 호출
# while True:

    # show()
    
        # 루프 지정된 간격으로 프레임을 갱신하는 함수를 호출
    