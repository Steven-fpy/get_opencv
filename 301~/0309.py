#0309.py

import cv2
import numpy as np

img = np.zeros(shape = (512, 512, 3),dtype = np.uint8) + 255
text = "So hungrry~~~~~~" 
text2 = "What's it Today's my meal~~???"
text3 = "May be....."
text4 = "Something special!!!"
text5 = "Wowwwwwwwwwwwwwww~~~~"
text6 = "Super great!!!!!!!"



org = (50, 100)
org2 = (50, 150)
org3 = (50, 200)
org4 = (50, 250)
org5 = (50, 300)
org6 = (50, 350)




font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText(img, text, org, font, 1, (255, 0, 0), 2)
cv2.putText(img, text2, org2, font, 1, (255, 0, 150), 2)
cv2.putText(img, text3, org3, font, 1, (200, 50, 50), 2)
cv2.putText(img, text4, org4, font, 1, (150, 75, 125), 2)
cv2.putText(img, text5, org5, font, 1, (50, 200, 255), 2)
cv2.putText(img, text6, org6, font, 1, (0, 255, 0), 2)

size, baseline = cv2.getTextSize(text, font, 1, 2)

pts1 = (org[0] + size[0], org[1] - size[1])


cv2.rectangle(img, org, (org[0] + size[0], org[1] - size[1]),
				(0, 0, 255))
cv2.circle(img, org, 3, (0, 255, 0), 2)

cv2.circle(img, pts1, 3, (0, 255, 0), 2)


cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
