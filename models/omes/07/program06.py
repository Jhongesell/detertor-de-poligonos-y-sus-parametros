#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:26:16 2021
Hue. de 0 a 179 \ matiz
Saturation: de 0 a 255 \saturacion
Value: de 0 a 255 \brillo o valor
[H,S,V]
@author: jhongvp
"""

import cv2
import numpy as np

cap=cv2.VideoCapture(0)

blueBajo=np.array([100,100,20],np.uint8)
blueAlto=np.array([125,255,255],np.uint8)

while True:
    ret, frame=cap.read()
    if ret == True:
        frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskBlue=cv2.inRange(frameHSV,blueBajo,blueAlto)
        maskBluevis = cv2.bitwise_and(frame,frame, mask=maskBlue)
        cv2.imshow('maskBluevis',maskBluevis)
        cv2.imshow('maskBlue',maskBlue)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
cap.release()
cv2.destroyAllWindows()