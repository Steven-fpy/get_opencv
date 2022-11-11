#0502.py

import cv2
import numpy as np
src = cv2.imread('./data/srcThreshold.png',cv2.IMREAD_GRAYSCALE)
# src2 = cv2.imread('./data/SegmentTest.jpg',cv2.IMREAD_GRAYSCALE)

# dst = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)

# ret, dst = cv2.threshold(dst, 100, 255, cv2.THRESH_BINARY)


# grey = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(grey, 160, 255, cv2.THRESH_BINARY)
# mask_inv = cv2.bitwise_not(mask)
# cv2.imshow('mask', mask)

cv2.imshow('src', src)
# cv2.imshow('src2', src2)



ret, dst = cv2.threshold(src, 0, 255,
                        cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('dst', dst)



dst2 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 51, 7) #51 : 블록사이즈 인데 홀수로만
cv2.imshow('dst2',dst2) 
# src1_bg = cv2.bitwise_and(src, src, mask = mask)
# cv2.imshow('src1_bg',src1_bg)



dst3 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 51, 7)
cv2.imshow('dst3', dst3)

dst4 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, 51, 21 )
cv2.imshow('dst4', dst4)

dst5 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY, 51, 21 )
cv2.imshow('dst5', dst5)


cv2.waitKey()
cv2.destroyAllWindows()
