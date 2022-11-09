#0212-2.py

import cv2
import time

class Animator():

    def __init__(self, initFunc, updateFrameFunc, interval):
        self.__initFunc = initFunc
        self.__updateFrameFunc = updateFrameFunc
        self.__interval = interval

        # print('__updateFrameFunc: ', self.__updateFrameFunc)


    def show(self):

        # 처음으로 한번만 동작하는 초기화 함수를 호출
        self.__initFunc()

        # 루프, 지정된 간격으로 프레임을 갱신하는 함수를 호출
        frameCount = 1
        while True:
            # print('self: ', self)
            retval = self.__updateFrameFunc(frameCount)

            # if not retval:
            #     break

            # interval의 값만큼 지연
            # time.sleep(self.__interval / 1000)
            key = cv2.waitKey(self.__interval)
            if key == 27: #esc
                # 영상 정지 호출
                break

            frameCount += 1
            pass

        pass


displayText = ""

def videoInit():
    global displayText

    retval, frame = cap.read()

    # 여기에 문구를 합성
    displayText = "재생"

    org = (50, 100)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text=displayText, org=org, fontFace=font, fontScale=1, color=(255,0,0), thickness=2)

    cv2.imshow('video', frame)

def updateFrame(k):
    print('k: ', k)

    retval, frame = cap.read()
    if retval:
        cv2.imshow('video', frame)        

    return retval

def videoStop():

    retval, frame = cap.read()

    global displayText
    displayText = "정지"

    org = (50, 100)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text=displayText, org=org, fontFace=font, fontScale=1, color=(255,0,0), thickness=2)

    time.sleep(1)
    pass


cap = cv2.VideoCapture('./data/vtest.avi')

# print('updateFrame: ', updateFrame)

# 콜백함수를 연결
ani = Animator(videoInit, updateFrame, 50)

# show, 재생시작
ani.show() #블럭


if cap.isOpened():
    cap.release()
