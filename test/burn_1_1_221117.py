# 0424.py
import time
import cv2
import numpy as np
# from matplotlib import pyplot as plt

# plt.grid()

# plt.show()
# print(X)


src = cv2.imread('./data/ind.jpg')

dst = src.copy()
# dst[0:100, 200:300] = 255
# pt1 = 0,0
# pt2 = 495, 290
# cv2.rectangle(dst, pt1, pt2, (255,255 , 255), 1)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
i = 0
j = 71
l = 0
m = 45
k = 60
f = 0
j2 = 500
i2 = 300
for i in range(0,541):
    if i < 510:
        cv2.putText(dst, '175', (5,45), fontFace=font,fontScale=1, color=(0,0,255), thickness=2)

        cv2.putText(dst, '0', (l+5,f+105), fontFace=font,fontScale=1, color=(0,255,0), thickness=2)
        cv2.putText(dst, '0', (j+5,l+45), fontFace=font,fontScale=1, color=(0,255,0), thickness=2)
        cv2.putText(dst, '0', (j+5,l+105), fontFace=font,fontScale=1, color=(0,255,0), thickness=2)
        cv2.putText(dst, '0', (j+5,l+165), fontFace=font,fontScale=1, color=(0,255,0), thickness=2)
        cv2.putText(dst, '0', (j+5,l+225), fontFace=font,fontScale=1, color=(0,255,0), thickness=2)
        cv2.putText(dst, '0', (j+5,l+285), fontFace=font,fontScale=1, color=(0,255,0), thickness=2)


        cv2.line(dst, (j, i-10),(j, i2), (255, 255, 255), 1)
        cv2.line(dst, (l, k),(j2, k), (255, 255, 255), 1)

        # i -= 10
        j += 71
        f += 60
        k += 60
        
        # print('j', j)
        # print('i', i)
    # time.sleep(1)
    # if i == 540:
# for j in range(0,510):
        
    # if j < 510:
    
    #     cv2.line(dst, (j-20, i),(j2, i), (255, 255, 255), 1)
    #     i += 60

#         j += 71

# cv2.line(dst, (0, 60), (500, 60), (255, 255, 255), 1)
# cv2.line(dst, (0, 120), (500, 120), (255, 255, 255), 1)
# cv2.line(dst, (0, 180), (500, 180), (255, 255, 255), 1)
# cv2.line(dst, (0, 240), (500, 240), (255, 255, 255), 1)
# cv2.putText(dst, 'here', (i,j), fontFace=font,fontScale=1, color=(0,255,0), thickness=2)

# cv2.line(dst, (71, 0), (71, 300), (255, 255, 255), 1)
# cv2.line(dst, (142, 0), (142, 300), (255, 255, 255), 1)
# cv2.line(dst, (213, 0), (213, 300), (255, 255, 255), 1)
# cv2.line(dst, (284, 0), (284, 300), (255, 255, 255), 1)
# cv2.line(dst, (355, 0), (355, 300), (255, 255, 255), 1)
# cv2.line(dst, (426, 0), (426, 300), (255, 255, 255), 1)

# cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

















# X = np.array ([[0, 0, 0, 100, 100, 150, -100, -150],
#                 [0, 50, -50, 0, 30, 100, -20, -100]],
#                 dtype = np.float64)
# X = X.transpose()       # X = X.T

# cov, mean = cv2.calcCovarMatrix(X, mean = None,
#                                 flags = cv2.COVAR_NORMAL + 
#                                         cv2.COVAR_ROWS)
# # print('mean = ', mean)
# # print('cov = ', cov)
# ret, icov = cv2.invert(cov)
# # print('icov = ', icov)

# dst = np.full((512, 512, 3), (255, 255, 255), dtype = np.uint8)
# rows, cols, channel = dst.shape
# centerX = cols // 2
# centerY = rows // 2

# v2 = np.zeros((1, 2), dtype = np.float64)

# FLIP_Y = lambda y: rows - 1 - y         

# # draw Mahalanobis(mean, v2, icov)



# # draw X, Y-axes
# cv2.line(dst, (0, 256), (cols - 1, 256), (0, 0, 0))
# cv2.line(dst, (256, 0), (256, rows), (0, 0, 0))

# # calculate eigen vectors
# ret, eVals, eVects = cv2.eigen(cov)
# print('eVals = ', eVals)
# print('eVects = ', eVects)

# def ptsEigenVactor (eVal, eVect):
# ## global mX, centerX, centerY
#         scale = np.sqrt(eVal) #eVal[0]
#         x1 = scale * eVect[0]
#         y1 = scale * eVect[1]
#         x2, y2 = -x1, -y1

#         x1 += mean[0, 0] + centerX
#         y1 += mean[0, 1] + centerY
#         x2 += mean[0, 0] + centerX
#         y2 += mean[0, 1] + centerY
#         y1 = FLIP_Y(y1)
#         y2 = FLIP_Y(y2)
#         return int(x1), int(y1), int(x2), int(y2)

# #draw eVects[0]
# x1, y1, x2, y2 = ptsEigenVactor(eVals[0], eVects[0])
# cv2.line(dst, (x1, y1), (x2, y2), (0, 0, 0), 2)

# x1, y1, x2, y2 = ptsEigenVactor(eVals[0], eVects[1])
# cv2.line(dst, (x1, y1), (x2, y2), (0, 0, 0), 2)

# # v1 = np.array([[0], [0]], dtype = np.float64)
# # v2 = np.array([[0], [50]], dtype = np.float64)

# # dist = cv2.Mahalanobis(v1, v2, icov)
# # print('dist = ', dist)

# # src1 = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# # src2 = np.zeros(shape = (512,512), dtype = np.uint8) + 100
# # 
# # dst1 = src1 + src2
# # dst2 = cv2.add(src1, src2)
# # dst2 = cv2.add(src1, src2, dtype = cv2.CV_8U)

# # cv2.imshow('dst1', dst1)
# # cv2.imshow('dst2', dst2)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()




# # cv2.imshow('src',src)
# # cv2.waitKey()
# # cv2.destroyAllWindows()