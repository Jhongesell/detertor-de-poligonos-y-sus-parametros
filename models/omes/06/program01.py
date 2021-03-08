#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 23:16:33 2021

@author: jhongvp
"""

import cv2
import numpy as np

grises=np.zeros((500,600),dtype=np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(grises, 'Humbral: T=130',(100,70), font, 1.5,(255),2,cv2.LINE_AA)

grises[100:300,:200]=130
grises[100:300,200:400]=20
grises[100:300,400:600]=210
grises[300:600,:200]=35
grises[300:600,200:400]=255
grises[300:600,400:600]=70
grises2=grises.copy()
cv2.putText(grises,'130',(60,150), font, 1,(255),1,cv2.LINE_AA)
cv2.putText(grises,'20',(280,150), font, 1,(255),1,cv2.LINE_AA)
cv2.putText(grises,'210',(470,150), font, 1,(0),1,cv2.LINE_AA)
cv2.putText(grises,'35',(70,350), font, 1,(255),1,cv2.LINE_AA)
cv2.putText(grises,'255',(270,350), font, 1,(0),1,cv2.LINE_AA)
cv2.putText(grises,'70',(480,350),font, 1,(255),1,cv2.LINE_AA)
cv2.putText(grises,'130>T?',(40, 230), font, 1, (255),1,cv2.LINE_AA)
cv2.putText(grises,'20>T?',(250,230),font,1,(255),1,cv2.LINE_AA)
cv2.putText(grises,'210>T?',(440,230),font,1,(0),1,cv2.LINE_AA)
cv2.putText(grises,'35>T?',(50,430),font,1,(255),1,cv2.LINE_AA)
cv2.putText(grises, '255>T?',(240,430),font,1,(0),1,cv2.LINE_AA)
cv2.putText(grises, '70>T?',(450,430),font,1,(255),1,cv2.LINE_AA)

_,binarizada=cv2.threshold(grises2,130,255,cv2.THRESH_BINARY) #130 señala el valor del humbral

cv2.imshow('Grises', grises)
cv2.imshow('Binarizada',binarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()

