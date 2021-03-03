#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:20:43 2021

@author: jhongvp
"""

import cv2
import numpy as np

def dibujar(mask,color):
    contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        area=cv2.contourArea(c)
        if area > 3000:
            x,y,w,h = cv2.boundingRect(c)
            if color == (255,0,0):
                cv2.rectangle(frame,(x,y),(x+w,y+h),color,3)
                cv2.line(frame,(x,y),(x+w,y+h),color,3)
                cv2.line(frame,(x+w,y),(x,y+h),color,3)
                cv2.putText(frame,'Azul',(x+10,y+10),font,0.75,color,2,cv2.LINE_AA)
            if color == (0,255, 255):
                M=cv2.moments(c)
                if (M["m00"]==0): M["m00"]=1
                xcentro=int(M["m10"]/M["m00"])
                ycentro=int(M['m01']/M["m00"])
                radio=xcentro+x
                #nuevoContorno=cv2.convexHull(c)
                cv2.circle(frame,(xcentro,ycentro),radio,color,3)
                cv2.putText(frame,'Amarillo',(x+10,y+10), font, 0.75,color,2,cv2.LINE_AA)
                #cv2.drawContours(frame,[nuevoContorno], 0, (0,255,0), 3)
                
cap=cv2.VideoCapture(0)

azulBajo = np.array([105,100,20],np.uint8)
azulAlto = np.array([125,255,255],np.uint8)

amarilloBajo = np.array([25,100,20],np.uint8)
amarilloAlto = np.array([35, 255, 255],np.uint8)

#redBajo1 = np.array([0,100,20],np.uint8)
#redAlto1 = np.array([5,255,255],np.uint8)

#redBajo2 = np.array([175, 100, 20],np.uint8)
#redAlto2 = np.array([179,255,255],np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, frame=cap.read()
    
    if ret==True:
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskAzul = cv2.inRange(frameHSV,azulBajo,azulAlto)
        maskAmarillo = cv2.inRange(frameHSV,amarilloBajo,amarilloAlto)
        #maskRed1 = cv2.inRange(frameHSV,redBajo1,redAlto1)
        #maskRed2 = cv2.inRange(frameHSV,redBajo2,redAlto2)
        #maskRed = cv2.add(maskRed1, maskRed2)
        dibujar(maskAzul,(255,0,0))
        dibujar(maskAmarillo,(0,255,255))
        #dibujar(maskRed,(0,0,255))
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
cap.release()
cv2.destroyAllWindows()