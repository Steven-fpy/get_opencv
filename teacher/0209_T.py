# 0209.py

import cv2
# from matplotlib import pyplot as plt

# pip install pafy
# pip install youtube_dl

# ..lib\site-packages\pafy\backend_youtube_dl.py", line 53
# like_count, dislike_count

import pafy
# url = 'http://www.youtube.com/watch?v=u_Q7Dkl7AIk'
url = 'https://www.youtube.com/watch?v=dalRStsPG0s&list=PL-BpxO3st_vmIw4YlWpbDG3FKJNCpWfaz'

video = pafy.new(url)
best = video.getbest()

cap = cv2.VideoCapture(best.url)
# cap = cv2.VideoCapture(url)
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

    cv2.imshow('frame', frame)

    red = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
    seeds = cv2.Canny(red, 100,200)
    cv2.imshow('seeds', red)


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,100,200)
    cv2.imshow('edges', edges)

    key = cv2.waitKey(25) #0.025, 40fps
    if key == 27: #esc
        break
    # time.sleep()
    pass

if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()

