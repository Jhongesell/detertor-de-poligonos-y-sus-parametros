#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 22:48:06 2021
SELECCIÓN DE CONTORNOS DE ACUERDO A CIERTA ÁREA
(Detect and tracking by color)
Detectar contornos de acuerdo al color, dibujar contornos al objeto identificado
limpieza de ruido
@author: jhongvp
"""

import cv2
import numpy as np

cap=cv2.VideoCapture(1)

verdeBajo=np.array([50,100,20],np.uint8)
verdeAlto=np.array([70,255,255],np.uint8)

#verdeBajo=np.array([85,100,20],np.uint8)
#verdeAlto=np.array([110,255,255],np.uint8)

while True:
    ret, frame=cap.read()
    if ret == True:
        frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskGreen=cv2.inRange(frameHSV,verdeBajo,verdeAlto)
        contornos,_ = cv2.findContours(maskGreen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(frame,contornos, -1, (0,255,0), 3)
        for c in contornos:
            area=cv2.contourArea(c)
            if area > 3000:
                cv2.drawContours(frame,[c], 0, (205,0,255), 2)
        cv2.imshow('maskGreen',maskGreen)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
cap.release()
cv2.destroyAllWindows()
