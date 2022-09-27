#Encontrando extremidades em contorno de regiões

'''
Este código poderá ser usado para encontrar a extremidade norte
sul, leste e oeste de uma região de contorno. 

Enquanto essa skill não é exatamente útil por si só, ela de vez 
em quando é usada como uma etapa de pré-processamento em aplicações
mais avançadas de visão computacional. 

Um ótimo exemplo dessa aplicação é reconhecimento de gestos.
'''

import os
import cv2
import imutils
import numpy as np

#Acessando um diretório
os.chdir("./Miscelanias/Imagens")

#Carregando e pré-processando a imagem
img = cv2.imread('extreme_points_input.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = cv2.GlaussianBlur(gray, (5,5),0)

#Pré-processamento para remover erosões e dilatações
thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)

#Encontrar contornos na imagem
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv2.contourArea)


#Encontrando pontos de extremidade no contorno
extLeft = tuple(c[c[:, :, 0].argmin()][0])      #Menor coordenada em x (ponto oeste)
extRight = tuple(c[c[:, :, 0].argmax()][0])     #Maior coordenada em x (ponto leste)
extTop = tuple(c[c[:, :, 1].argmin()][0])       #Menor coordenada em y (ponto sul)     
extBot = tuple(c[c[:, :, 1].argmax()][0])       #Maior coordenada em y (ponto norte)


#Desenhando a borda do objeto e, então desenhando
#cada ponto de extremidade.
cv2.drawContours(img, [c], -1, (0, 255, 255), 2)
cv2.circle(img, extLeft, 8, (0, 0, 255), -1)
cv2.circle(img, extRight, 8, (0, 255, 0), -1)
cv2.circle(img, extTop, 8, (255, 0, 0), -1)
cv2.circle(img, extBot, 8, (255, 255, 0), -1)

cv2.imshow("Image", img)
cv2.waitKey(0)