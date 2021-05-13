import cv2
import numpy as np

img = cv2.imread('resources/images/lena.png')



# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
#
# cv2.imshow("horizontal", imgHor)
# cv2.imshow("horizontal", imgVer)
cv2.waitKey(0)