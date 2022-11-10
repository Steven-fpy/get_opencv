import cv2

src = cv2.imread('./data/lena.jpg',cv2.IMREAD_GRAYSCALE)

x, y, w, h = cv2.selectROI("loca", src, False)
# print("x position, y position : ", x_pos, y_pos)
# print("width, height : ", width, height)

moisac = src[y : y+h, x:x + w]
moisac = cv2.blur(moisac, (10,50))
img = src
img[y:y+h, x:x+w] = moisac
cv2.destroyAllWindows()
cv2.imshow("Mosaic", img)

cv2.waitKey()
cv2.destroyAllWindows()