import cv2
import numpy as np

#warp perspective to get bird eye view

img = cv2.imread("resources/images/cards.jpg")

width, height = 250, 350

#define 4 corners of card
pts1 = np.float32([[111,219],[287,188],[154,482],[352, 440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("imshow", img )
cv2.imshow("output", imgOutput)

cv2.waitKey(0)