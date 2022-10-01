import os
import cv2
import time
import uuid

IMAGE_PATH = 'CollectedImages' #Stating the image path folder name.

labels = ['Hello', ' Yes', ' No', 'Thanks', 'Please'] #Stating all the different labels.

num_of_images = 10 #Stating the number of image captures to take for each individual label.

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label) #Creating individual folders for each label inside the CollectedImages folder. 
    os.makedirs(img_path, exist_ok=True) #Create the sub directories along with the already created directories; in case the already created directories are missing from the path.
    cap = cv2.VideoCapture(0)
    print(f"Collecting images for {label}")
    time.sleep(20)

    for img_num in range(num_of_images):
        success, frame = cap.read()
        image_name = os.path.join(f"{label}_{str(uuid.uuid1())}.jpg") #Create unique image name for all images.
        cv2.imwrite(os.path.join(img_path, image_name), frame)
        cv2.imshow('frame' , frame)
        time.sleep(1)
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()