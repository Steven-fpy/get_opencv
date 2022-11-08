# 0311.py
import os
import cv2
import numpy as np


def onMouse(event, x, y, flags, param):

	if event == cv2.EVENT_LBUTTONDOWN:
		if flags & cv2.EVENT_FLAG_SHIFTKEY:
			cv2.rectangle(param[0], (x - 5, y - 5),
							(x + 5, y + 1), (255, 0, 0))
		else:
			cv2.circle(param[0], (x,y), 5, (255, 0, 0), 3)

	elif event == cv2.EVENT_RBUTTONDOWN:
		cv2.circle(param[0], (x,y),5, (0,255,0),3)
	
	elif event == cv2.EVENT_LBUTTONDOWN:
		param[0] == np.zeros(param[0].shape, np.uint8) + 255

	elif event == cv2.EVENT_MBUTTONDOWN:
		cv2.rectangle(img, pt1,pt2, (255,255 , 255), -1)
	cv2.imshow("img", param[0])

img = np.zeros((512, 512, 3), np.uint8) + 255

pt1 = 0,0
pt2 = 1024, 1024
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse, [img])
cv2.waitKey()
cv2.destroyAllWindows()
		