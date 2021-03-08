#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:20:52 2021

@author: jhongvp
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:15:44 2021
Este programa carga una imagen y la descompone en sus 03 bandas de colores BGR
@author: jhongvp
"""

import cv2
import numpy as np

bgr=cv2.imread('prueba.jpg')
C1=bgr[:,:,0]
C2=bgr[:,:,1]
C3=bgr[:,:,2]

cv2.imshow('BGR',np.hstack([C1,C2,C3]))
cv2.waitKey(0)
cv2.destroyAllWindows()

