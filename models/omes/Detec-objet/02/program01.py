#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:16:06 2021

@author: jhongvp
"""

import cv2

image = cv2.imread('ave.jpeg')

cv2.imshow('Imagen',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
