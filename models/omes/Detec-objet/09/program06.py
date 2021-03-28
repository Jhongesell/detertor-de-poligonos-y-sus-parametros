#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 10:39:20 2021

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
cv2.putText(imagen,'Entrenando con OpenCV',(200,350),font,1,(0,0,0),2,cv2.LINE_AA)
"""cv2.putText(Imagen donde se va a visualizar, Texto, Ubicación, Fuente del texto,
Tamaño del texto, Color (BGR), Grosor, Tipo de línea"""


cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()