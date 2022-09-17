#Description: Converting color video to gray scale video

import cv2

cap = cv2.VideoCapture('Resources/elon.mp4')
while True:
    success, video = cap.read()
    print(video.shape)
    video_gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
    print(video_gray.shape)
    cv2.imshow('Gray_img', video_gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break