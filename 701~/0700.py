import numpy as np
import cv2 as cv



img = cv.VideoCapture(0)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# gray = img.astype(np.unit8)
gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)
gray = cv.cvtColor(img, cv.COLOR_RGB2BGR)


ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)


# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 2)


# sure background area
sure_bg = cv.dilate(opening,kernel,iterations=3)


# Finding sure foreground area
dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
result_dist_transform = cv.normalize(dist_transform, None, 255, 0, cv.NORM_MINMAX, cv.CV_8UC1)
ret, sure_fg = cv.threshold(dist_transform, 0.7*dist_transform.max(),255, cv.THRESH_BINARY)


# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg,sure_fg)


# Marker labelling
ret, markers = cv.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0


markers = cv.watershed(img, markers)

img[markers == -1] = [255, 0, 0]
img[markers == 1] = [255, 255, 0]

cv.imshow("dist_transform", result_dist_transform)
cv.imshow("unknown", unknown)
cv.imshow("sure_fg", sure_fg)
cv.imshow("sure_bg", sure_bg)
cv.imshow("result", img)
cv.waitKey(0)