#0710.py

import cv2
import numpy as np

#1
# src = cv2.imread('./data/hand.jpg')
src = cv2.VideoCapture(0)
# src = cv2.imread('./data/flower.jpg')
# src = cv2.imread('./data/lena.jpg')
# src = cv2.imread('./data/Penguins.jpg')
frame_size = (
    int(src.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(src.get(cv2.CAP_PROP_FRAME_HEIGHT)),
)
mask = np.zeros(shape=(frame_size[0], frame_size[1]), dtype=np.uint8)

# mask    = np.zeros(shape = src.shape[:2], dtype = np.uint8)
# 영상이라서 uint8사용
markers = np.zeros(shape = src.shape[:2], dtype = np.int32)
#비교값이라서 int32사용 (음수를 사용할수도 있기 때문)

# dst = src.copy()
# cv2.imshow('dst', dst)

#2
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(param[0], (x, y), 10, (255, 255, 255), -1)
            cv2.circle(param[1], (x, y), 10, (255, 255, 255), -1)
    cv2.imshow('dst', param[1])
# cv2.setMouseCallback('dst', onMouse, [mask, dst])

#3
mode =cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE




while True:
    cv2.setMouseCallback('dst', onMouse, [mask, dst])   #3-1
    key = cv2.waitKey(30)       #cv2.waitKeyEx(30)

    if key == 0x1B:         #ESC, 27
        break
    elif key == ord('r'):   # 3-2 ord 키를 가져오는 명령어
        mask[:, :] = 0
        dst = src.copy()
        cv2.imshow('dst', dst)
    elif key == ord(' '):   # 3-3
        contours, hierarchy = cv2.findContours(mask, mode, method)
        print('len(countours)= ', len(contours))
        markers[: ,:] = 0
        for i, cnt in enumerate(contours):
            cv2.drawContours(markers, [cnt], 0, i + 1, -1)
        cv2.watershed(src, markers)
        
        # -----------------watershed() 설명--------------------
        # 그레이스케일 이미지에서 높은 픽셀값을 가지는 부분을 언덕으로 보고, 
        # 낮은 픽셀 값을 가지는 부분을 계곡으로 보고,
        # 한 이미지에 여러개의 고립된 계곡(극소점)이 있을 수 있다.
        # 각각 다른 색의 물(라벨)로 물을 채운다고 했을때
        # markers 를 -1 로 주어 일종의 벽을 만든다.
        # (화소값은 양수이기 때문 -1을 주어 화소가 없다는 것을 표현)
        # 3-4
        dst = src.copy()
        dst[markers == -1] = [0, 0, 255]    #경계선
        # 따라서 붉은 색의 경계선이 생기게 된다.
        
        for i in range(len(contours)):      #분할영역
            r = np.random.randint(256)
            g = np.random.randint(256)
            b = np.random.randint(256)
            dst[markers == i + 1] = [b, g, r]
        # 그 영역을 랜덤한 색으로 채운다.
        # ----------------------여기 까지-----------------------
        dst = cv2.addWeighted(src, 0.4, dst, 0.6, 0)    #합성
        # 약간 흐릿한 색상으로 채워서 합성
        
        cv2.imshow('dst', dst)
cv2.destroyAllWindows()