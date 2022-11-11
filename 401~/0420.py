# 0420.py

import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# src2 = np.zeros(shape = (512,512), dtype = np.uint8) + 100

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(src)
print('src: ', minVal, maxVal, minLoc, maxLoc)

dst = cv2.normalize(src, None, 100, 200, cv2.NORM_MINMAX) # 최대 최소 범위가 작아서  차이가 작을수록 사진이 뿌옇게 보인다.
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(dst)
print('dst: ',minVal, maxVal, minLoc, maxLoc)

# dst1 = src1 + src2
# dst2 = cv2.add(src1, src2)
# dst2 = cv2.add(src1, src2, dtype = cv2.CV_8U)


cv2.imshow('dst', dst)
cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()
