# 0424.py

import cv2
import numpy as np

X = np.array ([[0, 0, 0, 100, 100, 150, -100, -150],
                [0, 50, -50, 0, 30, 100, -20, -100]],
                dtype = np.float64)
X = X.transpose()       # X = X.T

cov, mean = cv2.calcCovarMatrix(X, mean = None,
                                flags = cv2.COVAR_NORMAL + 
                                        cv2.COVAR_ROWS)
# print('mean = ', mean)
# print('cov = ', cov)
ret, icov = cv2.invert(cov)
# print('icov = ', icov)

dst = np.full((512, 512, 3), (255, 255, 255), dtype = np.uint8)
rows, cols, channel = dst.shape
centerX = cols // 2
centerY = rows // 2

v2 = np.zeros((1, 2), dtype = np.float64)

FLIP_Y = lambda y: rows - 1 - y         

#draw Mahalanobis(mean, v2, icov)
for y in range(rows):
        for x in range(cols):
                v2[0, 0] = x - centerX
                v2[0, 1] = FLIP_Y(y) - centerY  #y-축 뒤집기
                dist = cv2.Mahalanobis(mean, v2, icov)
                if dist < 0.1:
                        dst[y, x] = [50, 50, 50]
                elif dist < 0.3:
                        dst[y, x] = [100, 100, 100]
                elif dist < 0.8:
                        dst[y, x] = [200, 200, 200]
                else:
                        dst[y, x] = [250, 250, 250]

for k in range(X.shape[0]):
        x, y = X[k, :]
        cx = int(x + centerX)
        cy = int(y + centerY)                       
        cy = FLIP_Y(cy)
        cv2.circle(dst, (cx, cy), radius = 5,
                        color = ( 0, 0, 255), thickness = -1)

# draw X, Y-axes
cv2.line(dst, (0, 256), (cols - 1, 256), (0, 0, 0))
cv2.line(dst, (256, 0), (256, rows), (0, 0, 0))

# calculate eigen vectors
ret, eVals, eVects = cv2.eigen(cov)
print('eVals = ', eVals)
print('eVects = ', eVects)

def ptsEigenVactor (eVal, eVect):
## global mX, centerX, centerY
        scale = np.sqrt(eVal) #eVal[0]
        x1 = scale * eVect[0]
        y1 = scale * eVect[1]
        x2, y2 = -x1, -y1

        x1 += mean[0, 0] + centerX
        y1 += mean[0, 1] + centerY
        x2 += mean[0, 0] + centerX
        y2 += mean[0, 1] + centerY
        y1 = FLIP_Y(y1)
        y2 = FLIP_Y(y2)
        return int(x1), int(y1), int(x2), int(y2)

#draw eVects[0]
x1, y1, x2, y2 = ptsEigenVactor(eVals[0], eVects[0])
cv2.line(dst, (x1, y1), (x2, y2), (255, 0, 0), 2)

x1, y1, x2, y2 = ptsEigenVactor(eVals[0], eVects[1])
cv2.line(dst, (x1, y1), (x2, y2), (255, 0, 0), 2)

# v1 = np.array([[0], [0]], dtype = np.float64)
# v2 = np.array([[0], [50]], dtype = np.float64)

# dist = cv2.Mahalanobis(v1, v2, icov)
# print('dist = ', dist)

# src1 = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# src2 = np.zeros(shape = (512,512), dtype = np.uint8) + 100
# 
# dst1 = src1 + src2
# dst2 = cv2.add(src1, src2)
# dst2 = cv2.add(src1, src2, dtype = cv2.CV_8U)

# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
