# 0612.py

import cv2
import numpy as np

src = cv2.imread('./data/alphabet.bmp', cv2.IMREAD_GRAYSCALE)
tmp_A = cv2.imread('./data/A.bmp', cv2.IMREAD_GRAYSCALE)
tmp_S =  cv2.imread('./data/S.bmp', cv2.IMREAD_GRAYSCALE)
tmp_b =  cv2.imread('./data/b.bmp', cv2.IMREAD_GRAYSCALE)
tmp_L = cv2.imread('./data/L.jpg', cv2.IMREAD_GRAYSCALE)
tmp_V = cv2.imread('./data/V.jpg', cv2.IMREAD_GRAYSCALE)
tmp_i = cv2.imread('./data/i.jpg', cv2.IMREAD_GRAYSCALE)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

#1
R1 = cv2.matchTemplate(src, tmp_A, cv2.TM_SQDIFF_NORMED)
minVal, _, minLoc, _ = cv2.minMaxLoc(R1)
print('TM_SQDIFF_NORMED: ', minVal, minLoc)

h, w = tmp_A.shape[:2]
cv2.rectangle(dst, minLoc, (minLoc[0] + w, minLoc[1] + h), (255, 0, 0), 2)

#2
R2 = cv2.matchTemplate(src, tmp_S, cv2.TM_CCORR_NORMED)
_, maxVal, _, maxLoc = cv2.minMaxLoc(R2)
print('TM_CCORR_NORMED: ', maxVal, maxLoc)

h, w = tmp_S.shape[:2]
cv2.rectangle(dst, maxLoc, (maxLoc[0] + w, maxLoc[1] + h), (0, 255, 0), 2)

#3
R3 = cv2.matchTemplate(src, tmp_b, cv2.TM_CCOEFF_NORMED)
_, maxVal, _, maxLoc = cv2.minMaxLoc(R3)
print('TM_CCOEFF_NORMED: ', maxVal, maxLoc)

h, w = tmp_b.shape[:2]
cv2.rectangle(dst, maxLoc, (maxLoc[0] + w, maxLoc[1] + h), (0, 0, 255), 2)

#4
R4 = cv2.matchTemplate(src, tmp_L, cv2.TM_CCOEFF_NORMED)
_, maxVal, _, maxLoc = cv2.minMaxLoc(R4)
print('TM_CCOEFF_NORMED_L: ', maxVal, maxLoc)

h, w = tmp_L.shape[:2]
cv2.rectangle(dst, maxLoc, (maxLoc[0] + w, maxLoc[1] + h), (255, 0, 255), 2)

#5
R5 = cv2.matchTemplate(src, tmp_V, cv2.TM_CCOEFF_NORMED)
_, maxVal, _, maxLoc = cv2.minMaxLoc(R5)
print('TM_CCOEFF_NORMED_V: ', maxVal, maxLoc)

h, w = tmp_V.shape[:2]
cv2.rectangle(dst, maxLoc, (maxLoc[0] + w, maxLoc[1] + h), (100, 200, 255), 2)

#6
R6 = cv2.matchTemplate(src, tmp_i, cv2.TM_CCOEFF_NORMED)
_, maxVal, _, maxLoc = cv2.minMaxLoc(R6)
print('TM_CCOEFF_NORMED_i: ', maxVal, maxLoc)

h, w = tmp_i.shape[:2]
cv2.rectangle(dst, maxLoc, (maxLoc[0] + w, maxLoc[1] + h), (100, 100, 100), 2)


cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

