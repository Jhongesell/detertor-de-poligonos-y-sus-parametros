#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 11:24:50 2021

@author: jhongvp
"""

import cv2
import numpy as np

imagen=255*np.ones((400,600,3),dtype=np.uint8) #255 para que la imagen se nos muestre en blanco

# Dibujando linea
cv2.line(imagen,(0,400),(600,0),(255,0,0),4)
"""cv2.line(
IMagen donde se va a visualizar,
Punto inicial,
Punto final,
Color (BGR),
Grosor de línea)"""

# Dibujando rectángulo
cv2.rectangle(imagen,(50,80),(140,140),(0,255,0),-1)
cv2.rectangle(imagen,(150,150),(300,300),(0,255,255),5)

# Dibujando círculo
cv2.circle(imagen,(520,150),70, (255,255,0),-1) # el último argumento como -1 significa que la figura se rellena completamente

"""cv2.circle(
Imagen donde se va a visualizar,
Punto central,
Radio,
Color (BGR),
Grosor)"""

# insertar texto
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen,'texto 1',(200,20),0,1,(0,0,0),2,cv2.LINE_AA)
cv2.putText(imagen,'texto 2',(200,50),1,1,(0,0,0),2,cv2.LINE_AA)
cv2.putText(imagen,'texto 3',(200,150),2,1,(0,0,0),2,cv2.LINE_AA)
cv2.putText(imagen,'textp 4',(200,250),3,1,(0,0,0),2,cv2.LINE_AA)
cv2.putText(imagen,'texto 5',(200,330),4,1,(0,0,0),2,cv2.LINE_AA)
cv2.putText(imagen,'texto 6',(200,350),5,1,(0,0,0),2,cv2.LINE_AA)
cv2.putText(imagen,'texto 7',(200,380),6,1,(0,0,0),2,cv2.LINE_AA)
cv2.putText(imagen,'texto 8',(100,100),7,1,(0,0,0),2,cv2.LINE_AA)

"""Fuentes:
    FONT_HERSHEY_SIMPLEX = 0
    FONT_HERSHEY_PLAIN = 1
    FONT_HERSHEY_DUPLEX = 2
    FONT_HERSHEY_COMPLEX = 3
    FONT_HERSHEY_TRIPLEX = 4
    FONT_HERSHEY_COMPLEX_SMALL = 5
    FONT_HERSHEY_SCRIPT_SIMPLEX = 6
    FONT_HERSHEY_SCRIPT_COMPLEXT = 7"""

"""cv2.putText(Imagen donde se va a visualizar, Texto, Ubicación, Fuente del texto,
Tamaño del texto, Color (BGR), Grosor, Tipo de línea"""


cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()