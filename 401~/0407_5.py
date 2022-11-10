# 0407.py

import cv2

src = cv2.imread('./data/lena.jpg',cv2.IMREAD_GRAYSCALE)
roi = cv2.selectROI(src)
print('roi', roi)

N = 64  #8, 32, 64
# height, width = src.shape
# height, width, channel = src.shape
# height = src.shape[0]
# width = src.shape[1]
height, width = src.shape[0:2]

bh = height // N
bw = width // N
# img = src.copy()    # 추가한것

def mosaic(src, roi, bh, bw):
    img = src.copy()
    if roi !=(0,0,0,0):
        roiX, roiY, roiW, roiH = roi

# height, width
        for y in range(roiY, roiY + roiH, bh): #range(start, stop, step)#이부분
        
            for x in range(roiX, roiX + roiW, bw):                      #이부분
            
                blockROI = src[y:y + bh, x:x + bw]
                img[y:y + bh, x:x + bw] = cv2.mean(blockROI)[0] # [B,G,R]


    return img

if roi !=(0,0,0,0):
    roiX, roiY, roiW, roiH = roi
    
    img = mosaic(src, roi, bh, bw, cv2.IMREAD_GRAYSCALE)

    #roi = (x축 y축 넓이 높이)

# 512/64


# for y in range(startY, endY, h): #range(start, stop, step)#이부분
#     for x in range(startX, endX, w):                      #이부분


    img = src.copy()
    img[roiY:roiY + roiH, roiX:roiX + roiW]

    # cv2.imshow('img', img)
    cv2.imshow('img', img)
    cv2.waitKey()

cv2.destroyAllWindows()