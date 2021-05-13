import cv2
import numpy as np

img = np.zeros((512, 512,3), np.uint8)
print(img.shape)

#img[:] = 255,0,0
#create line  begin  end        color    thickness
cv2.line(img, (0,0),(300,300), (0,255,0), 3)
cv2.line(img, (0,0),(img.shape[1],img.shape[0]), (0,255,0), 3)

#rectangle
cv2.rectangle(img, (0,0),(500,200), (0,0,255), cv2.FILLED)
#circle         center  radius    color
cv2.circle(img,(400, 50), 30,   (255,255,0), 5)
#                                               font              scale color   thickness
cv2.putText(img, "open CV ", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0), 3)

cv2.imshow("Image", img)

cv2.waitKey(0)


