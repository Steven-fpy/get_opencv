# 0211.py

import cv2
import matplotlib.pyplot as plt

#1				## 키보드 이벤트(key_press_event)를 처리 함수를 handle_key_press()로 설정한다. [ESC]를 누르면
				##cap.release()로 비디오 객체를 해제하고, plt.close()로 창을 파괴한다.
def handle_key_press(event):
	if event.key == 'escape':
		cap.release()
		plt.close()
def handle_close(evt):
	print('Close figure!')
	cap.release()

#2 프로그램 시작

cap = cv2.VideoCapture(0)					#0번 카메라

plt.ion()									#대화 모드 설정
fig = plt.figure(figsize=(10, 6))			#fig.set_size_inches(10,6)
plt.axis('off')
#ax = fig.gca()
#ax.set_axis_off()
fig.canvas.manager.set_window_title('Video Capture')
fig.canvas.mpl_connect('key_press_event', handle_key_press)
fig.canvas.mpl_connect('close_event', handle_close)
retval, frame = cap.read()			#첫 프레임 캡쳐
im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

#3

while True:
	retval, frame = cap.read()		#프레임 캡쳐
	if not retval:
		break
#	plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
	im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
	fig.canvas.draw()
#	fig.canvas.draw_idle()
	fig.canvas.flush_events()		#plt.pause(0.001)

if cap.isOpened():
	cap.release()