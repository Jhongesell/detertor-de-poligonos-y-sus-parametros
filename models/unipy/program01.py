import cv2

img = cv2.imread('image01.png',0)
ret, thresh = cv2.threshold(img,127,255,0)
#image,contours, hierarchy = cv2.findContours(thresh,1,2)
contours, hierarchy = cv2.findContours(thresh,1,2)


cnt = contours[0]
M = cv2.moments(cnt)
#print(M)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

area = cv2.contourArea(cnt)
perimetro = cv2.arcLength(cnt,True)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print("Los momentos son: ",str(M))
print("El centroide en x es: ", str(cx))
print("El centroide en y es: ", str(cy))
print("El área es: ", str(area))
print("El perimetro es: ", str(perimetro))
