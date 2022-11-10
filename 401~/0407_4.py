# 0407.py

import cv2

src = cv2.imread('./data/lena.jpg',cv2.IMREAD_GRAYSCALE)
roi = cv2.selectROI(src)
print('roi', roi)

dst = src.copy()    # 추가한것

if roi != (0, 0, 0, 0):
    img = src[roi[1]:roi[1] +roi[3],
                roi[0]:roi[0] + roi[2]]


N = 64  #8, 32, 64
# height, width = src.shape
# height, width, channel = src.shape
# height = src.shape[0]
# width = src.shape[1]
height, width = src.shape[0:2]

# 512/64
h = height // N
w = width // N

rect = [(200,200), 200, 200]

startY = rect[0][0] #200
startX = rect[0][1] #200 
endY = startY + rect[1] #400
endX = startX + rect[2] #400

# for y in range(startY, endY, h): #range(start, stop, step)#이부분
#     for x in range(startX, endX, w):                      #이부분
for y in range(roi(startY)): #range(start, stop, step)#이부분

    for x in range(roi(startX)):                      #이부분

        roi = src[y:y + h, x:x + w]
        dst[y:y + h, x:x + w] = cv2.mean(roi)[0:3] # [B,G,R]






    # cv2.imshow('img', img)
    cv2.imshow('img', dst)
    cv2.waitKey()

cv2.destroyAllWindows()