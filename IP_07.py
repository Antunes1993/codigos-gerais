#Rotação de imagens (da forma correta) usando OpenCV. 
'''
Quando fazemos rotação de imagens, temos que ter cuidado com a função cv2.rotate, pois ela pode cortar
partes da imagem. 
Isso poderá afetar negativamente um algoritmo de detecção de imagens por exemplo, caso usemos imagens
que foram rotacionadas de maneira incorreta e, por conta disso, estão com partes faltando.
'''

'''
Neste exemplo será discutido os problemas comuns que podem ocorrer quando rotacionamos imagens com 
OpenCV em Python. 

Especificamente, será examinado o problema que ocorre quando os cantos da imagem são cortados durante
o processo de rotação. 
'''

import os 
import cv2
import imutils
import numpy as np 


#Carregando a imagem
pathRef = "/home/leonardo/Projetos/Projetos/codigos-gerais/Miscelanias/Imagens"
os.chdir(pathRef)
img = cv2.imread('pill_01.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(blur, 20, 100)


#Rotação Incorreta

for angle in np.arange(0, 360, 15):
    rotated = imutils.rotate(img, angle)
    cv2.imshow("Rotacao Problematica", rotated)  
    cv2.waitKey(0)


#Rotação Correta
for angle in np.arange(0, 360, 15):
    rotated = imutils.rotate_bound(img, angle)
    cv2.imshow("Rotacao Correta", rotated)
    cv2.waitKey(0)


'''
Então, isso significa que sempre devemos usar .rotate_bound em vez do .rotate? 
O que faz dele tão especial? 
E o que está debaixo do capô?

Primeiramente, vamos começar dizendo que não há nada de errado com as funções cv2.getRotationMatrix2D e 
cv2.warpAffine. 

Na realidade, essas funções nos dão mais liberdade do que talvez estejamos acostumados (algo comparável com
gerenciamento manual de memória com C versus automatic garbage collection com Java). 

cv2.getRotationMatrix2D não se importa se a imagem for cortada. 

O tutorial abaixo contém a descrição matemática da função .rotate_bound, e demonstrando a utilização
da função cv2.getRotationMatrix2D dentro dessa própria função (e adicionalmente corrigindo o problema de corte
das bordas das imagens).

https://www.pyimagesearch.com/2017/01/02/rotate-images-correctly-with-opencv-and-python/
'''
