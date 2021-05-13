import cv2
import numpy as np

def empty(a):
    pass
path = 'resources/images/lambo.png'

cv2.namedWindow('trackbars')
cv2.resizeWindow('trackbars', 640, 240)
cv2.createTrackbar("hue minimum", "trackbars", 0, 179, empty)
img = cv2.imread(path)

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


cv2.imshow("original", img)
cv2.imshow("hsv", imgHSV)



cv2.waitKey(0)

