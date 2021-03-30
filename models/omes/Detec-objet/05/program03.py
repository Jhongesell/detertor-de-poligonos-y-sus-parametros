#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:15:44 2021
Programa que muestra 03 canales de colores, imprime imagen de RGB
y una segunda imagen de BGR
@author: jhongvp
"""

import cv2
import numpy as np

bgr=cv2.imread('figure04.jpeg')
C1=bgr[:,:,0]
C2=bgr[:,:,1]
C3=bgr[:,:,2]
cv2.imshow('BGR',np.hstack([C1,C2,C3]))

rgb=cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)
C1=rgb[:,:,0]
C2=rgb[:,:,1]
C3=rgb[:,:,2]
cv2.imshow('RGB',np.hstack([C1,C2,C3]))
cv2.waitKey(0)
cv2.destroyAllWindows()

