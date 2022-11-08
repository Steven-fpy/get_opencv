#0212.py

import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#프로그램시작
cap = cv2.VideoCapture(0)
fig = plt.figure(figsize=(10,6))
fig.canvas.manager.set_window_title('Video Capture')
plt.axis('off')

def show(self):
	# 처음으로 초기화 함수를 호출

	#루프 지정된 간격으로 프레임을 갱신하는 함수를 호출
	

def init():
	global im
	retval, frame = cap.read()
	im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

def updateFrame(k):
	# global im
	retval, frame = cap.read()
	if retval:
		cv2.
		# im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

ani = animation.FuncAnimation(fig, updateFrame, init_func = init,
								interval = 50)
plt.show()
if cap.isOpened():
	cap.release()

	#retval = return value