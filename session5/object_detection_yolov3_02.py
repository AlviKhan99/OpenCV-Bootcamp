#Description: Using YOLOV3 pre-trained weights for object detection.

#Importing Libraries:
import cv2
import numpy as np

#Capturing real-time observations using webcam:
cap = cv2.VideoCapture(0)

#Define required variables for YOLOV3 pre-trained model:
class_file = "yolov3/coco.names" #All the coco.names classes are inside this path.
class_name = [] #All the class names will be stored in this empty list.
whT = 320 #Weight, height, Target stated as they got the same value in this case.
confidence_threshold = 0.5 #Setting minimum confidence threshold for yolov3 object detection.
nms_threshold = 0.3 #nms: Non-maximum suppression, is used to reduce overlapped object detection.
model_configuration_path = "yolov3/yolov3-tiny.cfg" #Storing model configuration path in a variable.
model_weights_path = "yolov3/yolov3-tiny.weights" #Storing model weights path in a variable.

#Process to store all class names in class_name empty list variable:
with open(class_file, 'rt') as f:
    class_name = f.read().rstrip('\n').split('\n')

# print(class_name)

#Create the network (It means loading the model with the model weights and configuration)
net = cv2.dnn.readNetFromDarknet(model_configuration_path, model_weights_path)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV) #Setting OpenCV in the backend.
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU) #Setting the program on the CPU.

print("Done")

#Create findObjects function
def findObjects(outputs, img):
    #Define image height, width and channel
    hT, wT, cT = img.shape #Note: webcam captured images are colorful so channel is always 3 in this case.
    #Create empyty list to extract and store image bounding boxes
    bounding_box = []
    #Create empyty list to extract and store image class IDs
    classIDs = []
    #Create empyty list to extract and store image confidence scores
    confidence_score = []

    #Create for loop for output in outputs and detect objects in output in nested output within the for loop
    for output in outputs:
        for detection in output:
            conf_scores = detection[5:] #Extract confidence scores for all objects.
            classID = np.argmax(conf_scores) #Extract class ID with highest confidence from confidence scores using np.argmax().
            confidence = conf_scores[classID] #Storing confidence score of the highest confidence class ID.

            #If statement where if confidence score > confidence threshhold, show the object as detected.
            if confidence > confidence_threshold:
                w, h = int(detection[2] * wT), int(detection[3] * hT) #Getting object width and height.
                x, y = int((detection[0] * wT) - w/2), int((detection[1] * hT) - h/2) #Getting object x and y coordinates.
                bounding_box.append([x, y, w, h]) #Append bounding box empty list with object coordinates.
                classIDs.append(classID) #Append class IDs with highest confidence score class ID.
                confidence_score.append(float(confidence)) #Append confidence score with highest confidence score class ID.

            # print(len(bounding_box))
            #Applying Non-Maximum Suppression (NMS) to reduce overlapping
            indices = cv2.dnn.NMSBoxes(bounding_box, confidence_score, confidence_threshold, nms_threshold)

            #Calculate number of bounding boxes and draw the rectangle using a for loop
            for i in indices:
                box = bounding_box[i]
                x, y, w, h = box[0], box[1], box[2], box[3] 
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #Create bounding box rectangle.
                cv2.putText(img, f"{class_name[classIDs[i]].upper()} {int(confidence_score[i] * 100)}%", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,255), 2) #Put text with bounding boxes.





while True:
    success, img = cap.read()
    

    #Convert image to blob format. (For yolov3, images must be converted to blob format to use)
    blob = cv2.dnn.blobFromImage(img, 1/255, (whT,whT), [0,0,0], 1, crop=False)
    net.setInput(blob) #Set input to the network

    #Getting all layer names
    LayerName = net.getLayerNames()
    # print(LayerName)

    #Extracting only the last 3 output layers
    # print(net.getUnconnectedOutLayers()) #Printing last 3 output layer index points
    #Showing last 3 output layer names
    outputNames = [LayerName[i-1] for i in net.getUnconnectedOutLayers()]
    # print(outputNames)
    #Define network as a forward connection
    outputs = net.forward(outputNames)

    # print(len(output))
    # print(type(output))
    # print(type(output[0]))

    # print(output[0])
    # print(output[0].shape)
    # print(output[1].shape)
    # print(output[2].shape)
    
    # print(output[0][0])

    #Call findObjects function
    findObjects(outputs, img)


    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

