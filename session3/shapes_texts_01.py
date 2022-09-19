# Shape and text
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

img[:] = 255,0,0 #BGR 0,0,0

# Create a line
# cv2.line(img, (0,0), (300,400), (0,255,0), 3)
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 3)

### Rectangle
cv2.rectangle(img, (0,0), (250, 350), (0,255,0), 3)
# cv2.rectangle(img, (0,0), (250, 350), (0,255,0), cv2.FILLED)

### Create circle 
cv2.circle(img, (400,50), 50, (255,255,0), 4)

### Put texts
cv2.putText(img, "OpenCV Bootcamp", (200,440), cv2.FONT_HERSHEY_COMPLEX,1, (0,255,0), 1)

cv2.imshow('Image', img)
cv2.waitKey(0)