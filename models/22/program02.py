#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 15:50:39 2021

@author: jhongvp
"""


import cv2
print("la versión de OpenCV que se esta usando es"+str(cv2.__version__))

image = cv2.imread('images02.jpeg.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150)
#_, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2:]

for c in cnts:
    #area = cv2.contourArea(cnts)
    #print("El área es "+str(area)+" u2.")
    epsilon = 0.1*cv2.arcLength(c,True)
    perimetro=cv2.arcLength(c,True)
    print("===========================================")
    print("el perimetro es "+str(perimetro)+" unidades.")
    print("===========================================")
    approx = cv2.approxPolyDP(c, epsilon, True)
    
    cv2.drawContours(image, [c], 0, (0,255,0),2)
    cv2.imshow('image',image)
    cv2.waitKey(0)
    



#cv2.imshow('image',image)
#cv2.imshow('canny',canny)
#cv2.imshow('th',th)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("la versión de OpenCV que se esta usando es "+str(cv2.__version__))