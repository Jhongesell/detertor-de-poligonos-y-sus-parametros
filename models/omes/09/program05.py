#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 10:38:06 2021

@author: jhongvp
"""

import cv2
import numpy as np

imagen=255*np.ones((400,600,3),dtype=np.uint8) #255 para que la imagen se nos muestre en blanco

# Dibujando linea
cv2.line(imagen,(0,0),(600,400),(255,0,0),4)
"""cv2.line(
IMagen donde se va a visualizar,
Punto inicial,
Punto final,
Color (BGR),
Grosor de línea)"""

# Dibujando rectángulo
cv2.rectangle(imagen,(50,80),(100,100),(0,255,0),-1)
cv2.rectangle(imagen,(250,150),(300,300),(0,255,255),5)

# Dibujando círculo
cv2.circle(imagen,(400,150),70, (255,255,0),-1) # el último argumento como -1 significa que la figura se rellena completamente

"""cv2.circle(
Imagen donde se va a visualizar,
Punto central,
Radio,
Color (BGR),
Grosor)"""

cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()