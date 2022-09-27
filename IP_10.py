#Encontrando formas com background preto em imagens 

'''
Baseado na imagem finding_shapes_example.png, esse código servirá para:
1. Reconhecer as figuras com background preto. 
2. Se duas ou mais figuras se sobreporem elas devem ser todas tratadas como um único objeto.
3. Contar o número de regiões pretas. 
'''

import os
import cv2
import imutils
import numpy as np

#Acessando um diretório
os.chdir("C:\\Users\\feoxp7\\Desktop\\Códigos\\Miscelanias\\Imagens")

#Carregando imagem
img = cv2.imread('finding_shapes_example.png')

#Limites de cor mínima e máxima 
lower = np.array([0, 0, 0])         #Cor preta
upper = np.array([15, 15, 15])      #Cor cinza escuro

#Mascara - encontramos os pixels que estão dentro dos limites de cores especificados nas linhas acima.
shapeMask = cv2.inRange(img, lower, upper)

cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print("I found {} black shapes".format(len(cnts)))


#Exibição de imagem

# loop over the contours
for c in cnts:
	# draw the contour and show it
	cv2.drawContours(img, [c], -1, (0, 0, 255), 2)
	cv2.imshow("Image", img)
	cv2.waitKey(0)


