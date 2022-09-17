#Description: Cropping colored video

import cv2

cap = cv2.VideoCapture('Resources/elon.mp4')
while True:
    success, video = cap.read()
    print(video.shape)
    crop_video = video[0:100,1:500]
    cv2.imshow('Crop_Output', crop_video)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break