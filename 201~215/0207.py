# 0207.py

import cv2
# from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('./data/vtest.avi')
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (
    int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
)
print('frame_size =', frame_size)

while True:
    retval, frame = cap.read()

    if not retval:
        break

    cv2.imshow('frame', frame)                          #정상출력    

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    #이곳을 풀면 외곽선이 된다
    edges = cv2.Canny(gray,100,200)                   #이곳을 풀면 외곽선이 된다
    cv2.imshow('edges', edges)                        #이곳을 풀면 외곽선이 된다

    key = cv2.waitKey(25) #0.025, 40fps
    if key == 27: #esc
        break
    # time.sleep()
    pass

if cap.isOpened():
    cap.release()
# cap.release()
cv2.destroyAllWindows()

