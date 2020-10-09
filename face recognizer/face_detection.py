# Detect the face and named it if it is already stored in our dataset

import cv2
import numpy as np
from PIL import Image
import os

def draw_boundary(img,classifier,scaleFactor,minNeigbors,color,text,clf):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_image,scaleFactor,minNeigbors)

    coords = []

    for(x,y,w,h) in features:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        id,pred = clf.predict(gray_image[y:y+h,x:x+w])
        confidence = int(100*(1-pred/300))

        if confidence>77:
            if id == 1:
                cv2.putText(img,"Thanh",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,color,1,cv2.LINE_AA)
            if id == 2:
                cv2.putText(img,"Quan",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,color,1,cv2.LINE_AA)
            if id == 3:
                cv2.putText(img,"Hang",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,color,1,cv2.LINE_AA)
        else:
            cv2.putText(img,"UNKNOWN",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),1,cv2.LINE_AA)
      
        coords = [x,y,w,h]

    return coords 

def recognize(img,clf,faceCascade):
    coords = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
    return img

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.xml")

video_capture = cv2.VideoCapture(0)

while True:
    ret,img = video_capture.read()
    img = recognize(img,clf,faceCascade)
    cv2.imshow("face detection", img)

    if cv2.waitKey(1) == 13:
        break

video_capture.release()
cv2.destroyAllWindows()

# crop face, convert it to gray image ---> classifier
# to draw rectangle, we have to give our real images that come from the webcam