# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 22:06:24 2019

@author: CAPTAIN
"""

import cv2

eye=cv2.CascadeClassifier('haarcascade_eye.xml')
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile=cv2.CascadeClassifier('haarcascade_smile.xml')




def detect(gray,color):
    
    faces=face.detectMultiScale(gray,1.3,5)
    
    for (x,y,w,h) in faces:
        
        cv2.rectangle(color, (x,y),(x+w,y+h),(255,0,0),2)

        roi_gray = gray[y:y+h,x:x+w]
        roi_color= color[y:y+h,x:x+w]
        
        eyes= eye.detectMultiScale(roi_gray,1.2,3)
        
        for (ex,ey,ew,eh) in eyes:
            
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
        
        smiles= smile.detectMultiScale(roi_gray,1.5,5)
        
        for (sx,sy,sw,sh) in smiles:
            
            cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
            
    return color
    







video=cv2.VideoCapture(0)

while True:
    _,frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    abc=detect(gray, frame)
    
    cv2.imshow("SMILE PLEASE",abc)
    
    if cv2.waitKey(1) & 0XFF==ord('q'):
        video.release()
        cv2.destroyAllWindows()