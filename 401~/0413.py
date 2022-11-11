#0413.py

import cv2
src = cv2.imread('./data/lena.jpg')

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
yCrCv = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)      #YUV방식
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

cv2.imshow('gray', gray)
cv2.imshow('yCrCv',yCrCv)
cv2.imshow('hsv', hsv)

cv2.waitKey()
cv2.destroyAllWindows()

# 1 로 입력되고 2로 출력
# 1  to  2
# BGR2GRAY      
# GRAY2BGR      
# BGR2HSV       
# HSV2BGR       
# BGR2YCrCb     
# YCrCb2BGR     

