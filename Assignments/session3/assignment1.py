#Description: Applying warp perspective to the docs images in resources

import cv2
import numpy as np

width , height = 400, 600


img = cv2.imread("Resources\docs.jpg")

points1 = np.float32([[718,30],[1108,18],[746,560],[1219,550]])
points2 = np.float32([[0,0], [width, 0], [0,height], [width, height]])

matrix = cv2.getPerspectiveTransform(points1, points2)
img_out = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Documents', img)
cv2.imshow('warped document', img_out)

cv2.waitKey(0)