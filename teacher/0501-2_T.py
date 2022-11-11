#0501.py
import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
# cap2 = cv2.VideoCapture(0)

# rows, cols, channel = cap2
# roi = cap[0:rows, 0:cols]

# grey = cv2.cvtColor(cap2, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(grey, 160, 255, cv2.THRESH_BINARY)
# mask_inv = cv2.bitwise_not(mask)
# cv2.imshow('mask', mask)

# cap_bg = cv2.bitwise_and(roi, roi, mask = mask)
# cv2.imshow('src1_bg',cap_bg)

# src2_fg = cv2.bitwise_and(cap2, cap2, mask = mask_inv)
# cv2.imshow('src2_fg',src2_fg)

# dst = cv2.bitwise_or(cap_bg, src2_fg)
# cv2.imshow('dst', dst)

# cap[0:rows, 0:cols] = dst

while True:
    retval, frame = cap.read()
    if not retval:
        break

    dst = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # dst2 = cv2.cvtColor(frame, cv2.COLOR_BGR2LUV)
    # dst3 = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL)



    # ret, dst = cv2.threshold(dst, 120, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret, dst = cv2.threshold(dst, 100, 255, cv2.THRESH_BINARY)
    
    # roi = frame[0:rows, 0:cols]
    
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(grey, 160, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    src2_fg = cv2.bitwise_and(frame, frame, mask = mask_inv)
    src1_bg = cv2.bitwise_and(frame, frame, mask = mask)
    
    dst = cv2.bitwise_or(src1_bg, src2_fg)
    
    # cap = dst


    cv2.imshow('frame', frame)
    cv2.imshow('dst', dst)
    # cv2.imshow('dst2', dst2)
    # cv2.imshow('dst3', dst3)
    cv2.imshow('mask', mask)
    cv2.imshow('mask_inv', mask_inv)
    cv2.imshow('src2_fg', src2_fg)
    # cv2.imshow('result', cap)




    

    key = cv2.waitKey(25)
    if key == 27:
        break

cv2.destroyAllWindows()