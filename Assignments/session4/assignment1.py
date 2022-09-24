### Color extraction

import cv2
import numpy as np

path = "Resources\lena.png"

def empty():
    pass

cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 800, 250)
cv2.createTrackbar("Hue Min", "TrackBar", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBar", 0, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Val Min", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBar", 0, 255, empty)

while True:
    image = cv2.imread(path)
    image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #TrackBar objects
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBar")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBar")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBar")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBar")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBar")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBar")

    print(h_min, h_max, s_min, s_max, v_min, v_max)



    # lower = np.array([h_min,s_min,v_min])  #Hua min , Sat min, Val min
    lower = np.array([0,0,119])  #Hua min , Sat min, Val min
    # upper = np.array([h_max,s_max,v_max])  #Hue Max, Sat max, Val max
    upper = np.array([118,255,255])  #Hue Max, Sat max, Val max
   

    mask = cv2.inRange(image_HSV, lower, upper)

    image_result = cv2.bitwise_and(image, image,mask= mask)

    cv2.imshow("Original image", image)
    cv2.imshow("HSV image", image_HSV)
    cv2.imshow("mask image", mask)
    cv2.imshow("image_result", image_result)

    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break