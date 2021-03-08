#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:31:24 2021

@author: jhongvp

Este programa graba un vídeo
"""

import cv2

captura=cv2.VideoCapture('videoSalida.avi') #se pone el nombre del vídeo que queremos leer
#salida=cv2.VideoWriter('videoSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
while(captura.isOpened()):
    ret, imagen = captura.read()
    if ret==True:
        cv2.imshow('video',imagen)
        #salida.write(imagen)
        if cv2.waitKey(30) & 0xFF == ord('s'): #el valor de waitKey ayuda en la velocidad de reproduccion del video
            break
    else: break

captura.release()
#salida.release()
cv2.destroyAllWindows()