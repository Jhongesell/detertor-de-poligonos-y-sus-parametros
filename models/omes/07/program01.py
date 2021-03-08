#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:19:33 2021
Detección de colores en OpenCV
Hue. de 0 a 179 \ matiz
Saturation: de 0 a 255 \saturacion
Value: de 0 a 255 \brillo o valor
@author: jhongvp
"""

import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    if ret == True:
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
cap.release()
cv2.destroyAllWindows()
