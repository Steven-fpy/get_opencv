#0310.py

# from turtle import width
import cv2
import numpy as np

width, height = 1024, 1024
x, y, R = 512, 512, 100
x1,y1, R2 =	0 , 0, 50
direction = 0

# img = np.zeros(shape = (512, 512, 3),dtype = np.uint8) + 255
# text = "So hungrry~~~~~~" 

# org = (50, 100)

# font = cv2.FONT_HERSHEY_COMPLEX_SMALL
# cv2.putText(img, text, org, font, 1, (255, 0, 0), 2)

# cv2.rectangle(img, org, (org[0] + size[0], org[1] - size[1]),
# 				(0, 0, 255))
# cv2.circle(img, org, 3, (0, 255, 0), 2)

# K:V
#key : direction
KEY_MAP = {
	100: 0,	#오 , d
	115: 1,	#아 , s
	97: 2,	#왼 , a
	119: 3,	#위 , w
}

OFFSETS = {		#변위
	(10, 0),  #오
	(0, 10),  #아
	(-10, 0), #왼
	(0, -10), #위

}


while True:
	key = cv2.waitKeyEx(30)
	if key == 0x1B:
		break
#v2
# #방향키 전환
# direction = KEY_MAP[key]
direction = KEY_MAP.get(key, direction)

# 	elif key == 100:
# 		direction = 0
# 	elif key == 115:
# 		direction = 1
# 	elif key == 97:
# 		direction = 2
# 	elif key == 119:
# 		direction = 3

#방향으로 이동

offset = OFFSETS[direction]
x += offset[0]
y += offset[1]



	# for i in range(0,4):
	# 	i = 0
	# 	direction == 0
	# 	x += 20 
	# 	i + 1
	# 	direction == i
	# 	i = 1
	
	# if direction == 0:
	# 	x +=10
	# elif direction == 1:
	# 	y +=10
	# elif direction == 2:
	# 	x -=10
	# elif direction == 3:
	# 	y -=10
	# else:
	# 	y -= 10
	# if direction == 0:
	# 	x1 -=10
	# elif direction == 1:
	# 	y1 -=10
	# elif direction == 2:
	# 	x1 +=10
	# elif direction == 3:
	# 	y1 +=10
	# else:
	# 	y1 -= 10

#경계확인
	
	if x < R:
		x = R
		direction = 0
	
	if x > width - R:
		x = width - R
		direction = 2
	
	if y < R:
		y = R
		direction = 1
	
	if y > height - R:
		y = height - R
		direction = 3
	if x1 < R2:
		x1 = R2
		direction = 0
	
	if x1 > width - R2:
		x1 = width - R2
		direction = 2
	
	if y1 < R2:
		y1 = R2
		direction = 1
	
	if y1 > height - R2:
		y1 = height - R2
		direction = 3
	if x == x1 and y == y1:
		
# 지우고, 그리기

	img = np.zeros(shape = (1024, 1024, 3),dtype = np.uint8) + 255
	cv2.circle(img, (x,y), R, (0, 255, 0), -1)
	
	cv2.circle(img, (x1,y1), R2, (255, 0, 0), -1)

	cv2.imshow('img', img)

cv2.destroyAllWindows()
