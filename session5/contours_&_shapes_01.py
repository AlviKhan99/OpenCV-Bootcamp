# contours & shape detection
import cv2
import numpy as np


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 500:
            cv2.drawContours(img_contours, cnt , -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))

            objector = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            if objector == 3: objectType = "Triangle"
            elif objector == 4:
                aspratio = w/float(h)
                if aspratio > 0.95 and aspratio <1.05: objectType = "Square"
                else: objectType = "Rectangle"
            elif objector > 4: objectType = "Circle"
            else: objectType = "None"

            cv2.rectangle(img_contours, (x,y), (x+w, y+h), (255,255,0),3)
            cv2.putText(img_contours, objectType, (x+(w//2)-10, y+(h//2)-10),  cv2.FONT_HERSHEY_COMPLEX,0.5, (255,255,255), 2)

        




img = cv2.imread("Resources/shapes.png")
img_contours = img.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7), 1)
img_canny = cv2.Canny(img_blur, 50, 50)

getContours(img_canny)

cv2.imshow("original", img)
cv2.imshow("img gray", img_gray)
cv2.imshow("img_blur", img_blur)
cv2.imshow("img canny", img_canny)
cv2.imshow("img_contours", img_contours)

cv2.waitKey(0)