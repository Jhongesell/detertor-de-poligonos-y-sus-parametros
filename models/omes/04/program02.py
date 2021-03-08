#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:31:24 2021

@author: jhongvp

Este programa graba un vídeo
"""

import cv2

captura=cv2.VideoCapture(0) #capturar video desde una camara, 0 o -1; 1; 2
salida=cv2.VideoWriter('videoSalida01.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
while(captura.isOpened()):
    ret, imagen = captura.read()
    if ret==True:
        cv2.imshow('video',imagen)
        salida.write(imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

captura.release()
salida.release()
cv2.destroyAllWindows()
