#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:30:19 2021

@author: jhongvp
"""

import cv2

#imagen = cv2.imread('imagen01.jpg') # nos lee la imagen a color
imagen = cv2.imread('imagen01.jpg',0) # nos lee la imagen a grises
#imagen = cv2.imread('imagen01.jpg',1) # nos lee la imagen a color
cv2.imshow('Prueba de imagen', imagen)
cv2.waitKey(0) # nos presenta la imagen hasta que piquemos alguna tecla
#cv2.waitKey(1000) # nos presenta la imagen por 1 segundo
cv2.destroyAllWindows()
