#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:20:23 2019

@author: apple
"""

import cv2, sys, time
import face_recognition
import viVoicecloud as vv

vv.Login()
t = vv.tts()

img = cv2.imread("self1.jpg")

tags=[]
faces=[]

self3_img = face_recognition.load_image_file("self3.jpg")
#print(face_recognition.face_encodings(self3_img))
cbn3 = face_recognition.face_encodings(self3_img)[0]
faces = faces+[cbn3]
tags = tags+["cbn3"]
print("ok1")

cap = cv2.VideoCapture(0)
width = 640
height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
print("ok2")

while True:
    try:
        ret, frame = cap.read()#reading pictures from cam
        img = frame
        
        t1 = time.time()
        names = face_recognition.face_encodings(img)
        face_locations = face_recognition.face_locations(img)
        flag = 0
        
        for i in range(len(names)):
            faceCompare = face_recognition.compare_faces(faces,names[i], tolerance = 0.5)#higher, preciser
            try:
                faceIndex = faceCompare.index(True)
                print("Name:",tags[faceIndex])        
                t.say(text = "welcome championNan", voice = "John")
                print("ok3")
                if flag == 0:
                    cv2.imwrite("capture_self.jpg", img)
                    flag = flag+1
                
            except Exception as e:
                print("error in capturing:", e)
                print("Unknown")
                
    except Exception as e:
        print("Terminate by interuption:", e)
        cap.release()
        vv.Logout()
        sys.exit(0)
        


    
    

