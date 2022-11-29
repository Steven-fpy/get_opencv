#0710.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)

frame_size = (
    int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
)
print('frame_size =', frame_size)


mask = np.zeros(shape=(frame_size[0], frame_size[1]), dtype=np.uint8)
markers = np.zeros(shape=(frame_size[0], frame_size[1]), dtype=np.int32)

cv2.circle(mask, (10,10), 10, (255,255,255), -1)
cv2.circle(mask, (frame_size[0]//2,frame_size[1]//2), 10, (255,255,255), -1)

while True:
    retval, frame = cap.read()
    key = cv2.waitKey(30)

    if key == 0x1B:  #esc, 27
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    retval, gray = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    
    constours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print('len(countours)= ', len(constours))
    markers[: ,:] = 0
    for i, cnt in enumerate(constours):
        cv2.drawContours(markers, [cnt], 0, i + 1, -1)
    # cv2.watershed(cap, markers)



    dst = frame.copy()
    dst2 = dst.copy()
    cv2.drawContours(dst, constours, -1, (255, 255, 0), 2)
    cv2.imshow('dst', dst)
    cv2.imshow('dst2', dst2)
    cv2.imshow('dst3', dst2)
    cv2.imshow('dst4', dst)




    # constours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print('len(contours)=', len(constours))
    # markers[:,:] = 0 #초기화


    pass





cv2.destroyAllWindows()