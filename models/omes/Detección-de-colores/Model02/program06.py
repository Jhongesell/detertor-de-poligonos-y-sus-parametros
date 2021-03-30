import cv2
import numpy as np

def dibujar(mask,color):
    contornos,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        area=cv2.contourArea(c)
        perimetro=cv2.arcLength(c,True)

        if area > 2000:
            M=cv2.moments(c)
            if (M["m00"]==0): M["m00"]=1
            x=int(M["m10"]/M["m00"])
            y=int(M["m01"]/M["m00"])
            z1="area es: "+str(int(area))+"px**2"
            z2="perimetro es: "+str(int(perimetro))+"px"
            z3="el valor de c es: "+str(c)
            nuevoContorno=cv2.convexHull(c)
            cv2.circle(frame,(x,y),7,(0,255,0),-1)
            cv2.putText(frame,'{},{}'.format(x,y),(x+10,y),font,0.75,(0,255,0),1,cv2.LINE_AA)
            cv2.putText(frame,'{},{}'.format(z1,z2),(x-100,y-50),4,0.55,(200,200,0),1,cv2.LINE_AA)
            cv2.putText(frame,'{}'.format(z3),(x,y+50),5,0.55,(0,200,255),1,cv2.LINE_AA)
            cv2.drawContours(frame,[nuevoContorno],0,color,3)

cap=cv2.VideoCapture(1)
image01 = cv2.imread('figure03.jpeg') # imagen a leer

naranjaBajo = np.array([11,100,20],np.uint8)
naranjaAlto = np.array([20,255,255],np.uint8)

amarilloBajo = np.array([26,100,20],np.uint8)
amarilloAlto = np.array([32,255,255],np.uint8)

turquezaBajo = np.array([88,100,20],np.uint8)
turquezaAlto = np.array([92,255,255],np.uint8)

celesteBajo = np.array([93,100,20],np.uint8)
celesteAlto = np.array([99,255,255],np.uint8)

azulBajo = np.array([100,100,20],np.uint8)
azulAlto = np.array([125,255,255],np.uint8)


redBajo1 = np.array([0,100,20],np.uint8)
redAlto1 = np.array([5,255,255],np.uint8)

redBajo2 = np.array([175,100,20],np.uint8)
redAlto2 = np.array([179,255,255],np.uint)

font = cv2.FONT_HERSHEY_SIMPLEX
while True:

    ret,frame=cap.read()

    if ret==True:
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskAzul = cv2.inRange(frameHSV,azulBajo,azulAlto)
        maskAmarillo = cv2.inRange(frameHSV,amarilloBajo,amarilloAlto)
        maskRed1=cv2.inRange(frameHSV,redBajo1,redAlto1)
        maskRed2=cv2.inRange(frameHSV,redBajo2,redBajo2)
        maskRed=cv2.add(maskRed1,maskRed2)
        dibujar(maskAzul,(255,0,0))
        dibujar(maskAmarillo,(0,255,255))
        dibujar(maskRed,(0,0,255))
        cv2.imshow('frame',frame)
        cv2.imshow('imagen',image01)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
cap.release()
cv2.destroyAllWindows()

