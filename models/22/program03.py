#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:17:20 2021

@author: jhongvp
"""

import cv2
import numpy as np

img = cv2.imread('poligonos_n01_v03.png',0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hirearchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
print(M)