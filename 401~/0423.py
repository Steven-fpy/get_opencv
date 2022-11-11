# 0423.py

import cv2
import numpy as np

X = np.array ([[0, 0, 0, 100, 100, 150, -100, -150],
                [0, 50, -50, 0, 30, 100, -20, -100]],
                dtype = np.float64)
X = X.transpose()       # X = X.T

cov, mean = cv2.calcCovarMatrix(X, mean = None,
                                flags = cv2.COVAR_NORMAL + 
                                        cv2.COVAR_ROWS)
print('mean = ', mean)
print('cov = ', cov)

ret, icov = cv2.invert(cov)
print('icov = ', icov)

v1 = np.array([[0], [0]], dtype = np.float64)
v2 = np.array([[0], [50]], dtype = np.float64)

dist = cv2.Mahalanobis(v1, v2, icov)
print('dist = ', dist)

# src1 = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# src2 = np.zeros(shape = (512,512), dtype = np.uint8) + 100
# 
# dst1 = src1 + src2
# dst2 = cv2.add(src1, src2)
# dst2 = cv2.add(src1, src2, dtype = cv2.CV_8U)

# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
