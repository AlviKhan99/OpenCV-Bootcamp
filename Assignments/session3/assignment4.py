#Description: Joining images horizontally and vertically

import cv2
import numpy as np

img = cv2.imread('Resources/lambo.png')
resized_img = cv2.resize(img, (300, 200))

img1 = cv2.imread('Resources/robot.png')
resized_img1 = cv2.resize(img1, (300, 200))

img_horizontal = np.hstack((resized_img, resized_img1))
img_vertical = np.vstack((resized_img, resized_img1))

cv2.imshow("Images Joined Horizontally", img_horizontal)
cv2.imshow("Images Joined Vertically", img_vertical)
cv2.waitKey(0)