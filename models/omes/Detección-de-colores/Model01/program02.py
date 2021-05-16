import cv2
import numpy as np

cap=cv2.VideoCapture(1)
#python por defecto lee las imagenes en BGR

while True:
    ret, frame=cap.read()
    if ret==True:
        frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
cap.release()
cv2.destroyAllWindows()
