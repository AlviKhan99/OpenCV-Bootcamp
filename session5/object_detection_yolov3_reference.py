import cv2
import numpy as np

cap = cv2.VideoCapture(0)

class_file = "yolov3/coco.names"
clas_name = []
whT = 320 #width , height, target dimensions
confThreshold = 0.5 
nmsThreshold = 0.3
model_configuration = "yolov3/yolov3-tiny.cfg"
model_weights = "yolov3/yolov3-tiny.weights"

with open(class_file, 'rt') as f:
    clas_name = f.read().rstrip("\n").split('\n')

# print(clas_name)

## Creating netwotk 
net = cv2.dnn.readNetFromDarknet(model_configuration, model_weights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV) #setting openCV in Backend
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU) #setting on CPU

print("done")



def findObjects(outputs, img):
    hT, wT, cT = img.shape
    bbox = []
    classIDs = []
    confs = []  #confidence score 

    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]

            if confidence > confThreshold:
                w, h = int(det[2] * wT), int(det[3] * hT)
                x, y = int((det[0] * wT) - w/2), int((det[1] * hT) - h/2)
                bbox.append([x, y, w, h])
                classIDs.append(classId)
                confs.append(float(confidence))
    
    # print(len(bbox))
    ## Applying NMS to remove overlaps
    indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)

    for i in indices:
        box = bbox[i]
        x, y, w,h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(img, f"{clas_name[classIDs[i]].upper()} {int(confs[i] * 100)}%", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,255), 2)



while True:
    success, img = cap.read()

    #convert image to blob format 
    blob = cv2.dnn.blobFromImage(img, 1/255, (whT, whT), [0,0,0], 1, crop= False)
    net.setInput(blob)

    #Getting all layers name
    layerName = net.getLayerNames()
    # print(layerName)

    ## Keeping only last 3 output layers
    # print(net.getUnconnectedOutLayers())
    outputNames = [layerName[i-1] for i in net.getUnconnectedOutLayers()]
    # print(outputNames)
    outputs = net.forward(outputNames)

    # print(len(output))
    # print(type(output))
    # print(type(output[0]))

    # print(output[0])
    # print(output[0].shape)
    # print(output[1].shape)
    # print(output[2].shape)
    
    # print(output[0][0])

    findObjects(outputs, img)




    cv2.imshow("Image", img)
    cv2.waitKey(1)