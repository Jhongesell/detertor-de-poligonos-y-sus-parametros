#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:31:24 2021

@author: jhongvp
"""

import cv2

captura=cv2.VideoCapture(0) #capturar video desde una camara, 0 o -1; 1; 2

while(captura.isOpened()):
    ret, imagen = captura.read()
    if ret==True:
        cv2.imshow('video',imagen)
        if cv2.waitKey(1) & 0xFF == ord('A'):
            break

captura.release()
cv2.destroyAllWindows()