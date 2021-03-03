#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 22:53:27 2021

@author: jhongvp
"""

import cv2
import numpy as np

bgr=cv2.imread('prueba.jpg')

gris=cv2.cvtColor(bgr,cv2.COLOR_BGR2GRAY)

cv2.imshow('GRISES',gris)
cv2.waitKey(0)
cv2.destroyAllWindows()
