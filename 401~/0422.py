# 0422.py

import cv2
import numpy as np
import time

nPoints = 100
pts = np.zeros((1, nPoints, 2), dtype = np.uint16)
dst = np.full((512, 512, 3), (255, 255, 255), dtype = np.uint8)

while True:
    dst[:,:,:] = 255

    cv2.setRNGSeed(int(time.time()))
    
    cv2.randn(pts, mean = (256, 256), stddev = (50, 50))

# draw points
    for k in range(nPoints):
        x, y = pts[0][k, :]     #pts[0, k , :]
        cv2.circle(dst, (x,y), radius = 5, 
            color = (0, 0, 255), thickness = -1)

# src1 = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# src2 = np.zeros(shape = (512,512), dtype = np.uint8) + 100

# dst1 = src1 + src2
# dst2 = cv2.add(src1, src2)
# dst2 = cv2.add(src1, src2, dtype = cv2.CV_8U)


    cv2.imshow('dst', dst)
# while True:
    key = cv2.waitKey()
    if key == 32:
        break
#             cv2.imshow('dst', dst)
#         continue
# cv2.imshow('dst2', dst2)

cv2.destroyAllWindows()
