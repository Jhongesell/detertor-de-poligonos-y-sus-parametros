#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 10:04:46 2021
humbralización aplicado a una imagen
@author: jhongvp
"""

import cv2
import numpy as np
import imutils #permite redimensionar una imagen

image=cv2.imread('figure03.jpg',0)
image=imutils.resize(image,width=600)

_,binarizada=cv2.threshold(image,210,255,cv2.THRESH_BINARY) #el humbral es el 210
_,binarizadaInv=cv2.threshold(image,210,255,cv2.THRESH_BINARY_INV)
#_,Trunc=cv2.threshold(image,210,_,cv2.THRESH_TRUNC)
#_,Toz=cv2.threshold(image,210,_cv2.THRESH_TOZERO)
#_,TozInv=cv2.threshold(image,210,_,cv2.THRESH_TOZERO_INV)

cv2.imshow('Imagen',image)
cv2.imshow('Tipos: Binary - Binary Inv',np.hstack([binarizada,binarizadaInv]))
#cv2.imshow('Tipos: Trunc',trunc)
#cv2.imshow('Tipos: Tozero - Tozero Inv', np.hstack([Toz, TozInv]))
cv2.waitKey(0)
cv2.destroyAllWindows()
