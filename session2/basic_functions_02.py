### Basics functions
import cv2
import numpy as np

### 1. Convert to gray scale

# img = cv2.imread('Resources/lena.png')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img.shape)
# print(img_gray.shape)
# cv2.imshow('Color_img', img)
# cv2.imshow('Gray_img', img_gray)
# cv2.waitKey(0)


### Convert to blur 

# img = cv2.imread('Resources/lena.png')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
# cv2.imshow('Color_img', img)
# cv2.imshow('Gray_img', img_gray)
# cv2.imshow('Blur_img', img_blur)
# cv2.waitKey(0)



### 3. Convert to cannyImg

# img = cv2.imread('Resources/lena.png')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
# img_canny = cv2.Canny(img, 100, 100)
# cv2.imshow('Color_img', img)
# cv2.imshow('Gray_img', img_gray)
# cv2.imshow('Blur_img', img_blur)
# cv2.imshow('Canny_img', img_canny)
# cv2.waitKey(0)



### 4, Convert to dialation

kernel = np.ones((5,5), np.uint8)
print(kernel)
img = cv2.imread('Resources/lena.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
img_canny = cv2.Canny(img, 100, 100)
img_dialation = cv2.dilate(img_canny, kernel, iterations=1)
# erode
img_eroded = cv2.erode(img_dialation, kernel, iterations=2)
cv2.imshow('Color_img', img)
cv2.imshow('Gray_img', img_gray)
cv2.imshow('Blur_img', img_blur)
cv2.imshow('Canny_img', img_canny)
cv2.imshow('dialate_img', img_dialation)
cv2.imshow('eroded_img', img_eroded)
cv2.waitKey(0)
