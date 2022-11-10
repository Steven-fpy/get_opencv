# 0407.py

import cv2

src = cv2.imread('./data/lena.jpg',cv2.IMREAD_GRAYSCALE)
x, y, w, h = cv2.selectROI(src)
# print('roi', roi)
# dst = src.copy()

# if roi != (0, 0, 0, 0):         #(x, y, width, height)
#     img = src[roi[1]:roi[1] +roi[3],
#                 roi[0]:roi[0] + roi[2]]

sM = src[y : y+h, x:x + w]


N = 32
# height, width = src.shape                          #컬러

# height, width = src.shape[0:2]


h = h // N
w = w // N




# rect = roi

# for i in range(N):
#     for j in range(N):
#         # y = i * h+100
#         # x = j * w+100 
#         y = (y*h + i)
#         x = (x*w + y)
#         roi = src[y:y + h, x:x + w]
#         # rect = [(x, y), w, h]
#         # roi = img  
#         # roi = roi
#         # rect = cv2.selectROI(dst)

#         # src = roi
#         dst[y:y + h, x:x + w] = cv2.mean(roi)[0]      

# startY = rect[0][0]         #200
# startX = rect[0][1]         #200
# endY = startY + rect[1]     #400
# endX = startX + rect[2]     #400

for y in range(h):
    for x in range(w):
        roi = src[y:y + h, x:x + w]
        sM[y:y + h, x:x + w] = cv2.mean(roi)[0]



    # cv2.imshow('img', roi)
    cv2.imshow('img', sM)

    cv2.waitKey()

    cv2.destroyAllWindows()