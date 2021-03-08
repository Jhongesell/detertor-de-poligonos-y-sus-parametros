#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 22:08:58 2021
Programa que encierra los objetos de acuerdo a su color.
Objetivo es encerrar el color azul.
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
        #_,contornos,_ = cv2.findContours(maskBlue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contornos,_ = cv2.findContours(maskBlue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #maskBluevis = cv2.bitwise_and(frame,frame, mask=maskBlue)
        #cv2.imshow('maskBluevis',maskBluevis)
        cv2.drawContours(frame,contornos, -1, (255,0,0), 3)
        cv2.imshow('maskBlue',maskBlue)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
cap.release()
cv2.destroyAllWindows()