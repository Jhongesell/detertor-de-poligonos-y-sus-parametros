import cv2
import numpy as np

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
# Cargando imagen tipo PNG
#imagen = cv2.imread('images/png/imagen01.png')
#imagen = cv2.imread('images/png/imagen02.png')
#imagen = cv2.imread('images/png/imagen03.png')
#imagen = cv2.imread('images/png/imagen04.png') # Imprime error asociado al momento M
#imagen = cv2.imread('images/png/imagen05.png') # No es capaz de contar
#imagen = cv2.imread('images/png/imagen06.png')
#imagen = cv2.imread('images/png/imagen07.png')
#imagen = cv2.imread('images/png/imagen08.png')
imagen = cv2.imread('images/png/imagen09.png')

# Cargando imagen tipo JPG
#imagen = cv2.imread('images/jpg/imagen01.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpg/imagen02.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpg/imagen03.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpg/imagen04.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpg/imagen05.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpg/imagen06.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpg/imagen07.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpg/imagen08.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpg/imagen09.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpg/imagen10.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpg/imagen11.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpg/imagen12.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpg/imagen13.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpg/imagen14.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpg/imagen15.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('imagen05.jpg') # Imprime error asociado al momento M
#imagen = cv2.imread('imagen02.png')

# Cargando imagen tipo JPEG
#imagen = cv2.imread('images/jpeg/imagen01.jpeg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpeg/imagen02.jpeg') # Imprime error asociado al momento M
#imagen = cv2.imread('images/jpeg/imagen03.jpeg')

imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

maskAmarillo = cv2.inRange(imagenHSV, amarilloBajo, amarilloAlto)
maskVioleta = cv2.inRange(imagenHSV, violetaBajo, violetaAlto)
maskVerde = cv2.inRange(imagenHSV, verdeBajo, verdeAlto)
maskRojo1 = cv2.inRange(imagenHSV, rojoBajo1, rojoAlto1)
maskRojo2 = cv2.inRange(imagenHSV, rojoBajo2, rojoAlto2)
maskRojo = cv2.add(maskRojo1, maskRojo2)
maskCeleste = cv2.inRange(imagenHSV, celesteBajo, celesteAlto)
maskAzul = cv2.inRange(imagenHSV, azulBajo, azulAlto)
maskRosado = cv2.inRange(imagenHSV, rosadoBajo, rosadoAlto)
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
