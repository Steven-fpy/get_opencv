# 0421.py

import cv2
import numpy as np
import time

dst = np.full((512, 512, 3), (255, 255, 255), dtype = np.uint8)
nPoints = 100
pts = np.zeros((1, nPoints, 2), dtype = np.uint16)
cv2.setRNGSeed(int(time.time()))
cv2.randu(pts, (0, 0), (512, 512))

# draw points
for k in range(nPoints):
    x, y = pts[0, k][:]     #pts[0, k , :]
    cv2.circle(dst, (x,y), radius = 5, color = (0, 0, 255),
                thickness = -1)

# src1 = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# src2 = np.zeros(shape = (512,512), dtype = np.uint8) + 100

# dst1 = src1 + src2
# dst2 = cv2.add(src1, src2)
# dst2 = cv2.add(src1, src2, dtype = cv2.CV_8U)


cv2.imshow('dst', dst)
# cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
