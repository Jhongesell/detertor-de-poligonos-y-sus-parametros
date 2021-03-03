#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 10:07:47 2021

@author: jhongvp
"""

import cv2
import numpy as np

imagen=255*np.ones((400,600,3),dtype=np.uint8) #255 para que la imagen se nos muestre en blanco

cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()