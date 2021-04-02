import cv2
import numpy as np

# Espectros de colores BGR
amarilloBajo = np.array([20, 100, 20], np.uint8)
amarilloAlto = np.array([32, 255, 255], np.uint8)

violetaBajo = np.array([130, 100, 20], np.uint8)
violetaAlto = np.array([145, 255, 255], np.uint8)

verdeBajo = np.array([36, 100, 20], np.uint8)
verdeAlto = np.array([70, 255, 255], np.uint8)

rojoBajo1 = np.array([0, 100, 20], np.uint8)
rojoAlto1 = np.array([10, 255, 255], np.uint8)
rojoBajo2 = np.array([175, 100, 20], np.uint8)
rojoAlto2 = np.array([180, 255, 255], np.uint8)

celesteBajo = np.array([85, 100, 20], np.uint8)
celesteAlto = np.array([100, 255, 255], np.uint8)

azulBajo = np.array([101, 100, 20], np.uint8)
azulAlto = np.array([126, 255, 255], np.uint8)

rosadoBajo = np.array([145, 100, 20], np.uint8)
rosadoAlto = np.array([155, 255, 255], np.uint8)

# Cargando imagen a utilizar
#imagen = cv2.imread('image01.jpg')
#imagen = cv2.imread('image02.jpg')
imagen = cv2.imread('image03.jpg')
#imagen = cv2.imread('figure01.jpg')
#imagen = cv2.imread('figure02.jpeg')
#imagen = cv2.imread('figure03.jpeg')

imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Detectando colores
maskAmarillo = cv2.inRange(imagenHSV, amarilloBajo, amarilloAlto)
maskVioleta = cv2.inRange(imagenHSV, violetaBajo, violetaAlto)
maskVerde = cv2.inRange(imagenHSV, verdeBajo, verdeAlto)
maskRojo1 = cv2.inRange(imagenHSV, rojoBajo1, rojoAlto1)
maskRojo2 = cv2.inRange(imagenHSV, rojoBajo2, rojoAlto2)
maskRojo = cv2.add(maskRojo1, maskRojo2)
maskCeleste = cv2.inRange(imagenHSV, celesteBajo, celesteAlto)
maskAzul = cv2.inRange(imagenHSV, azulBajo, azulAlto)
maskRosado = cv2.inRange(imagenHSV, rosadoBajo, rosadoAlto)

# Dectectando contornos
contornosAmarillo = cv2.findContours(maskAmarillo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
#cv2.drawContours(imagen, contornosAmarillo, -1, (0,255,255),2)
cv2.drawContours(imagen, contornosAmarillo, -1, (3,100,100),2)


# Mostrando ventanas
cv2.imshow('02. maskAmarillo',maskAmarillo)
cv2.imshow('07. maskVioleta',maskVioleta)
cv2.imshow('03. maskVerde',maskVerde)
cv2.imshow('01. maskRojo',maskRojo)
cv2.imshow('04. maskCeleste',maskCeleste)
cv2.imshow('05. maskAzul', maskAzul)
cv2.imshow('06. maskRosado', maskRosado)

cv2.imshow('Imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
