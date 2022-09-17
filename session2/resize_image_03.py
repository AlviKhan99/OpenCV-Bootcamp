#### Cropping & Resizing Image
import cv2

img = cv2.imread('Resources/lambo.png')
# print(img.shape)
# resized_img = cv2.resize(img, (300, 200))
# print(resized_img.shape)
# cv2.imshow('Output', img)
# cv2.imshow('Resized_Output', resized_img)
# cv2.waitKey(0)


### Croping Image
crop_img = img[0:200,200:500]
cv2.imshow('Output', img)
cv2.imshow('Crop_Output', crop_img)
cv2.waitKey(0)