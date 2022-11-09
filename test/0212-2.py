#0212-2.py

import cv2
import time

class Animator():

    def __init__(self, initFunc, updateFrameFunc, interval):
        self.__initFunc = initFunc     #self.__initFunc(원래 없는 것을 만들면 파이썬은 생성시킨다) = initFunc
        self.__updateFrameFunc = updateFrameFunc
        self.__interval = interval
        # 파이썬은 클래스를 만들고 호출하면 __init__ 이라는 함수가 자동으로 호출된다. 위는 그걸 이용하여 
        # __init__ 이라는 함수에 오버라이딩 하여  self.__initFunc = initFunc 이하를 실행되게 한 것이다.
    
        print('__updateFrameFunc', self.__updateFrameFunc) #주소값을 찍어보면 아래의 updateFrame 과 같다.
    
    def show(self):
        # self.__initFunc.isOpened()
        # print('self._initFunc',a)
        # initFunc = initFunc
        # updateFrameFunc = updateFrameFunc
        # interval = interval
        # print('self.__updateFrameFunc', b)
        
        #처음으로 한번만 동작하는 초기화 함수를 호출
        self.__initFunc()

        # 루프 지정된 간격으로 프레임을 갱신하는 함수를 호출
        frameCount = 1
        while True:
            print('self:',self)
            retval = self.__updateFrameFunc(frameCount)
            
            # if not retval:
            #     break
            # interval의 값만큼 지연
            # time.sleep(self.__interval / 1000) #오류가 발생할수 있다.
            key = cv2.waitKey(self.__interval) #waitkey설명을 잘 살펴보면 밀리세컨 단위로 딜레이가 걸린다는 사실을 알수 있다.
            if key == 27: #esc
                #영상 정지 호출
                break
            
            elif key == 32: #space
                videoStop()
            # elif key == 115:
            #     videoStop()
                continue
                # pass
      
            # elif key == 97:
            #     video()
            #     pass
            # elif key == 119:
            #     videoStop()
            #     pass
            
            
            frameCount += 1
            pass
        pass

displayText = ""
    
def videoInit():
    retval, frame = cap.read()
    
    displayText = "PLAY"
    org = (50, 100)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(frame, text=displayText, org=org, fontFace=font, fontScale=1, color=(255,0,0), thickness=2)
        
    cv2.imshow('video', frame)

def updateFrame(k):
    print('updateFrame: k: ', k)
    
    retval, frame = cap.read()
    if retval:
        cv2.imshow('video', frame)
        global displayText
        displayText = "<<< PLAY"
        
        org = (50, 100)
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(frame, text=displayText, org=org, fontFace=font, fontScale=1, color=(255,0,0), thickness=2)

        cv2.imshow('video', frame)        

    return retval
        
def videoStop():
    retval, frame = cap.read()

    global displayText
    displayText = " | |  PAUSE"

    org = (50, 100)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    
    cv2.putText(frame, text=displayText, org=org, fontFace=font, fontScale=1, color=(255,0,0), thickness=2)


    cv2.imshow('video', frame)

    cv2.waitKey()
    pass

# def videoTap():




print('updateFrame', updateFrame) #주소값을 찍어보면 위의 self.__updateFrameFunc 와 같다.

cap = cv2.VideoCapture('./data/vtest.avi')
retval, frame = cap.read()
cv2.imshow('video', frame)

# 콜백함수를 연결
ani = Animator(videoInit, updateFrame, 50)
# ani = Animator()

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
    