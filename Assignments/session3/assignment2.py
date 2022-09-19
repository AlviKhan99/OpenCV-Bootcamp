#Description: Displaying triangle, square and ellipse
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

img[:] = 255,255,0

# Create a triangle
p1 = (100, 200)
p2 = (50, 50)
p3 = (300, 100)
  
cv2.line(img, p1, p2, (255, 0, 0), 3)
cv2.line(img, p2, p3, (255, 0, 0), 3)
cv2.line(img, p1, p3, (255, 0, 0), 3)

# Create a square
cv2.rectangle(img, (400,400), (300,300), (255,0,0), 3)

# Create an ellipse
cv2.ellipse(img,(150,300),(100,50),0,0,360,(255,0,0), 3)

cv2.imshow('Image',img)
cv2.waitKey(0)