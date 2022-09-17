#### Reading an Image

import cv2

# img = cv2.imread('Resources/lena.png')
# print(img.shape)
# cv2.imshow('Output', img)
# cv2.waitKey(0)

### Reading videos

# cap = cv2.VideoCapture('Resources/elon.mp4')
# while True:
#     success, img = cap.read()
#     print(img.shape)
#     cv2.imshow('Output', img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


#### Reading Webcam

cap = cv2.VideoCapture(0)

cap.set(3, 640) # set width
cap.set(4, 480) # set height

while True:
    success, img = cap.read()
    print(img.shape)
    cv2.imshow('Output', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
