#Criação de um módulo para alinhamento de perspectiva de imagens à 4 pontos.

'''
Este código poderá ser usado para transformar o campo de visão que o usuário tem de uma imagem, de maneira
que uma região de interesse dessa imagem possa ser vista de cima. 
'''

import os
import cv2
import imutils
import numpy as np 

'''
A função abaixo recebe uma lista com 4 pontos especificando as coordenadas (x,y) de cada ponto de um retângulo.
É crucial que tenhamos pontos do retângulo ordenados consistentemente. A ordem atual pode ser arbitrária desde 
que seja consistente durante a implementação. 

Neste exemplo seguiremos com: 
    Superior Esquerda
    Superior Direita
    Inferior Direita
    Inferior Esquerda

Após alocar a memória para os 4 pontos (rect = np.zeros((4,2),dtype = "float32")), nós iremos encontrar o ponto 
superior da esquerda, que deverá ter o menor valor de soma x+y. 
Em seguida iremos encontrar o ponto inferior direito que deverá ter o maior valor de soma x+y.

É claro que agora nós temos que encontrar os pontos superior direito e inferior esquerdo. Aqui nós iremos tomar 
a diferença entre os pontos x e y, usando a função diff. 

As coordenadas associadas à menor diferença será o ponto superior direito enquanto a maior diferença será associada
ao ponto inferior esquerdo. 

'''
def order_points(pts):
    print ("Detecção dos pontos: ")
    print ("-------------------------")
    #Inicializa uma lista de coordenadas (uma para cada um dos 4 pontos).
    rect = np.zeros((4,2), dtype = "float32")

    #O ponto superior esquerdo terá a menor soma, enquanto o ponto inferior direito
    #terá a maior soma. 
    s = np.sum(pts,axis=1)
    print ("Soma: ", s)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    print ("Máxima soma: ", rect[2])
    print ("Mínima soma: ", rect[0])
    print ("-------------------------")

    #Computando a diferença entre os pontos. O ponto superior direito terá a menor 
    #diferença, enquanto o ponto inferior esquerdo terá a maior diferença
    diff = np.diff(pts, axis = 1)
    print ("Diferença: ", diff)

    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]


    print ("Máxima diferença: ", rect[3])
    print ("Mínima diferença: ", rect[1])
    
    print ("-------------------------")
    print ("")
    #Retorna as coordenadas
    return rect



def four_point_transform(image, pts):
    #Obter a ordem consistente dos pontos e extraí-los individualmente
    rect = order_points(pts)
    (topLeft, topRight, bottomRight, bottomLeft) = rect 

    print ("Confirmando os pontos: ", rect)

    #Computa o comprimento da nova imagem, que será a distância entre as coordenadas em x do bottomRight e do bottomLeft 
    #ou a distância entre as coordenadas em x do topRight e do topLeft. O comprimento da nova imagem será o maior valor
    #dentre esses dois. 
    widthA = np.sqrt(((bottomRight[0] - bottomLeft[0]) ** 2) + ((bottomRight[1] - bottomLeft[1]) ** 2))
    widthB = np.sqrt(((topRight[0] - topLeft[0]) ** 2) + ((topRight[1] - topLeft[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    #Computa a altura da nova imagem, que será a distância entre as coordenadas em y do topRight e do bottomRight
    #ou a distância entre as coordenadas em y do topLeft e do bottomLeft. O comprimento da nova imagem será o maior valor
    #dentre esses dois. 
    heightA = np.sqrt(((topRight[0] - bottomRight[0]) ** 2) + ((topRight[1] - bottomRight[1]) ** 2))
    heightB = np.sqrt(((topLeft[0] - bottomLeft[0]) ** 2) + ((topLeft[1] - bottomLeft[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    #Agora que nós temos as dimensões da nova imagem, construa o conjunto de pontos de destino para obter uma vista de cima
    #da imagem, novamente especificando os pontos na ordem topLeft, topRight, bottomRight e bottomLeft. 
    dst = np.array([
        [0, 0],                                     #topRight
        [maxWidth - 1, 0],                          #topLeft
        [maxWidth - 1, maxHeight - 1],              #bottomRight
        [0, maxHeight - 1]], dtype = "float32")     #bottomLeft


    print ("Confirmando os pontos de destino: ", dst)
    print ("-------------------------")
    print ("")
    
    #Computar a matriz de transformação de perspectiva e aplica-la. 
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped


#Acessando um diretório
os.chdir("C:\\Users\\feoxp7\\Desktop\\ESTUDO\\codigos-gerais\\Miscelanias\\Imagens\\")

#Carregando e pré-processando a imagem
img = cv2.imread('Fig2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Pré-processamento para remover erosões e dilatações
thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)
#Encontrar contornos na imagem
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

i = 0
for c in cnts: 
    #Desenhando a borda do objeto
    cv2.drawContours(img, [c], -1, (0, 255, 255), 2)
    i += 1
    print ("CARD NUMERO: ", i)
    #Encontrando pontos de extremidade no contorno
    extLeft = tuple(c[c[:, :, 0].argmin()][0])      #Menor coordenada em x (ponto oeste)
    extRight = tuple(c[c[:, :, 0].argmax()][0])     #Maior coordenada em x (ponto leste)
    extTop = tuple(c[c[:, :, 1].argmin()][0])       #Menor coordenada em y (ponto sul)     
    extBot = tuple(c[c[:, :, 1].argmax()][0])       #Maior coordenada

    print ("extLeft:" , extLeft)
    print ("extRight:" , extRight)
    print ("extTop:" , extTop)
    print ("extBot:" , extBot)

    #Desenhando a borda do objeto e, então desenhando
    #cada ponto de extremidade.
    cv2.drawContours(img, [c], -1, (0, 255, 255), 2)  
    cv2.circle(img, extLeft, 8, (0, 0, 255), -1)        #Menor coordenada em x
    cv2.circle(img, extRight, 8, (0, 255, 0), -1)       #Maior coordenada em x
    cv2.circle(img, extTop, 8, (255, 0, 0), -1)         #Menor coordenada em y
    cv2.circle(img, extBot, 8, (255, 255, 0), -1)       #Maior coordenada em y
    print ('---------------------------')
    
    pts = [extLeft, extTop, extRight, extBot]
    warped = four_point_transform(img, pts)


    cv2.imshow("Image", img)
    cv2.imshow("Warped", warped)
    cv2.waitKey(0)
    


   #pts = [(62,91),(270,65),(293,294),(79,324)]