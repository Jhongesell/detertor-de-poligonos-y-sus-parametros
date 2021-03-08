#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 15:29:12 2021

@author: jhongvp
"""

import cv2

image = cv2.imread('poligonos_n01_v02.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150)
#_, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    cv2.drawContours(image, [c], 0, (0,255,0),2)
    cv2.imshow('image',image)
    cv2.waitKey(0)


cv2.imshow('image',image)
cv2.imshow('canny',canny)
#cv2.imshow('th',th)
cv2.waitKey(0)
cv2.destroyAllWindows()