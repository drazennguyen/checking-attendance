#1. Generate dataset
#2. Train the classifier and save it
#3. Detect the face and named it if it is already stored in our dataset

#!/usr/bin/env_python
import cv2
import os
from os import path
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def remove(string):
    return string.replace(" ","")

reader = SimpleMFRC522()
print("Put student card to read")

try:
    id, text = reader.read()
    stu_id = remove(text)
    
finally:
    GPIO.cleanup()

print("student id:")
print(stu_id)

# Leaf directory
directory = stu_id

# Parent directory
parent_dir = "/home/pi/Desktop/face recognizer/dataset2"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
os.makedirs(path)
    
print("Directory '% s' created" % directory)

def generate_dataset():
    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    def face_cropped(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray,1.3,5)
        # Scaling factor = 1.3
        # Minimum neighbor = 5
        
        if faces is ():
            return None
        for(x,y,w,h) in faces:
            cropped_face = img[y:y+h,x:x+w]
        return cropped_face
    
    cap = cv2.VideoCapture(0)
         
    # 1: Truong Thanh
    # 2: Anh Quan
    # 3: Thu Hang
    
    
    # id la mssv -> doc tu the rfid
    img_id = 0
    
    while True:
        ret,frame = cap.read()
        if face_cropped(frame) is not None:
            img_id += 1
            face = cv2.resize(face_cropped(frame),(200,200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            # check coi co mssv chua, chua thi tao thu muc mssv
            # dataset/mssv
#             file_name_path = "dataset/user." + str(stu_id) + "." + str(img_id) + ".jpg"
            file_name_path = "dataset2/" + stu_id + "/" + str(img_id) + ".jpg"
            cv2.imwrite(file_name_path, face)
            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            # (50,50) is the origin point from where text is to be written
            # font scale = 1
            # thickness = 2
            
            '''
            idea:
                dataset/
                    mssv1/
                        pic1
                        pic2
                        .
                        .
                        .
                        pic100
                        
                    mssv2/
                        pic1
                        pic2
                        .
                        .
                        .
                        pic100
                        
                    mssvn/
                
                classifier/
                    mssv1.xml
                    mssv2.xml
                    .
                    .
                    .
                    mssvn.xml
            '''
            
            cv2.imshow("Cropped face",face)
            if cv2.waitKey(1)==13 or int(img_id)==200:
                break
    cap.release()
    cv2.destroyAllWindows()
    print("Collecting samples is completed......")

        
generate_dataset()
            
