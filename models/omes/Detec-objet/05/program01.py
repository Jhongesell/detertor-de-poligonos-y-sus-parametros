#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:15:44 2021

@author: jhongvp
"""

import cv2
import numpy as np

bgr=np.zeros((400, 1000, 3),dtype = np.uint8) #fondo color negro
bgr[:,:,:]=(255,0,0) # para cambiar el color a azul
#bgr[:,:,:]=(255,0,100) # para cambiar el color a morado
cv2.imshow('BGR',bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
