#Description: Face detection in image and video 

import cv2
import numpy as np

haarcascade = "Resources/haarcascade_frontalface_default.xml"

#### Image Face Detection
image = cv2.imread('Resources/lena.png')

facecascade = cv2.CascadeClassifier(haarcascade)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = facecascade.detectMultiScale(image_gray, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(image ,(x,y), (x+w,y+h), (0,255,255), 2)

cv2.imshow('Face in Image', image)
cv2.waitKey(0)


#### Video Face Detection
cap = cv2.VideoCapture('Resources/elon.mp4')
while True:
    success, img = cap.read()

    facecascade = cv2.CascadeClassifier(haarcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = facecascade.detectMultiScale(img_gray, 1.1, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img ,(x,y), (x+w,y+h), (0,255,0), 2)


    cv2.imshow('Faces in Video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break










# cap = cv2.VideoCapture(0)

# cap.set(3, 640) # set width
# cap.set(4, 480) # set height

# while True:
#     success, img = cap.read()

#     facecascade = cv2.CascadeClassifier(haarcascade)
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     faces = facecascade.detectMultiScale(img_gray, 1.1, 4)

#     for (x,y,w,h) in faces:
#         cv2.rectangle(img ,(x,y), (x+w,y+h), (0,255,0), 2)

#     cv2.imshow("face",img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break