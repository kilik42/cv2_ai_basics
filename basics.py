import cv2
import numpy as np

print("package imported")
# read images
# img = cv2.imread("resources/images/color.jpg")
# cv2.imshow(img)
# cv2.waitKey(0) #0 means infinite delay   1000 means 1 second


#read video
# cap = cv2.VideoCapture("resources/videos/video.mp4")
# #we need  a while loop to go through the frames one by one
#
# while True:
#     #will save  image into img and tell if it was sucess or not
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# read webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)#width
# cap.set(4, 480)#height
# cap.set(10,100) #brightness of webcam
#
# while True:
#     #will save  image into img and tell if it was sucess or not
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#basic functions when building open cv projects
img = cv2.imread("resources/images/lion.jpg")
kernel = np.ones((5,5), np.uint8)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 100,100)
#dialtion make it thicker the lines
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
#erosion -- make it thinner
imgEroded = cv2.erode(imgDialation, kernel, iterations = 5)

cv2.imshow("Gray image", imgGray)
cv2.imshow("Blurred image", imgBlur)
cv2.imshow("canny", imgCanny)
cv2.imshow("dialation image", imgDialation)
cv2.imshow("erosion image", imgEroded)
cv2.waitKey(0)




