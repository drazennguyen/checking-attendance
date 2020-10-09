#!/usr/bin/env_python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import os

reader = SimpleMFRC522()
print("Put card to read")

def remove(string):
    return string.replace(" ","")


try:
    id, text = reader.read()
#     print(id)
    print(text)
    stu_id = remove(text)

finally:
    GPIO.cleanup()

print("student id:")
print(stu_id)

#leaf directory
directory = stu_id

#parent directory
parent_dir = "/home/pi/Desktop/face recognizer/dataset"

#Path
path = os.path.join(parent_dir, directory)

#create the directory
os.makedirs(path)
print("Directory '% s' created" % directory)
