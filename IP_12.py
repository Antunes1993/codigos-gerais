#Detecção de formatos 
'''
Este código poderá ser usado para rotular e identificar o 
formato de figuras em uma imagem a partir das suas 
propriedades de contorno. 
'''

'''
O primeiro passo para construirmos nosso detector de formas 
é encapsularmos a lógica de detecção de formas. 
'''

'''
Na classe abaixo, com intuito de performar a detecção de formas
nós iremos usar a aproximação de contorno. 
Como o nome sugere, a aproximação de contorno é um algorítimo
para reduzir o número de pontos em uma curva com um conjunto 
reduzido de pontos. 

Esse algoritmo é normalmente conhecido como Ramer-Douglas-Peucker
ou simplesmente algoritmo split-and-merge.

A aproximação do contorno é baseada na suposição de que uma curva
pode ser aproximada por uma série de segmentos de linha curta. 
Isso leva a uma curva aproximada resultante que consiste em um 
subconjunto de pontos que foram definidos pela curva original. 

A aproximação do contorno já está implementada no OpenCV por
meio do método cv2.approxPolyDP.

Para realizar a aproximação do contorno, primeiro calculamos o 
perímetro do contorno (peri = cv2.arcLength(c, True)), seguido 
por construir de fato a aproximação. 
'''

import os
import cv2 
import imutils

#A classe foi declarada dentro do código principal pois esse código tem propósitos apenas instrutivos.
class ShapeDetector:
    def __init__(sefl):
        pass

    def detect(self, c):                                    # c = contorno.
        shape = "Nao Identificado"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)     # range de valores comuns para o segundo parâmetro da função approxPolyDP = [1 ~ 5%] do perímetro do contorno.

        #Se forem identificados 3 vértices, temos um triângulo.
        if len(approx) == 3:
            shape = "triangulo"
		
        # Se forem identificados 4 vértices, temos um quadrado ou um retângulo.
        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            # um quadrado terá um ar próximo de 1. Caso contrário será um retângulo.
            shape = "Quadrado" if ar >= 0.95 and ar <= 1.05 else "Retangulo"
		
        # Se forem identificados 5 vértices, temos um pentágono.
        elif len(approx) == 5:
            shape = "Pentagono"

        # Do contrário, temos um círculo
        else:
            shape = "Circulo"

        #Retorna a string shape
        return shape

'''
É importante entender que o contorno consiste em uma lista de vértices. 
Nós podemos verificar o número de elementos nessa lista para determinar
o formato de um objeto. 
'''

#Acessa o diretório com a imagem
os.chdir("/home/leonardo/Projetos/Projetos/codigos-gerais/Miscelanias/Imagens")

#Carregamento e pré-processamento da imagem
img = cv2.imread('shapes_and_colors.jpg')
resized = imutils.resize(img, width=300)
ratio = img.shape[0]/float(resized.shape[0])

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

#Detectando contornos
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

#Instanciando a classe ShapeDetector
sd = ShapeDetector()

#Identificando cada contorno
for c in cnts:
    try:
        # Computando o centro do contorno e, então, detectando o nome
        # da forma usando apenas o contorno.
        M = cv2.moments(c)
        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)
        shape = sd.detect(c)
        # Multiplicando as coordenadas do contorno pelo ratio e então 
        # desenhando os contornos e o nome da forma na imagem. 
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
        cv2.putText(img, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
        cv2.imshow("Imagem", img)
        cv2.waitKey(0)
    except: 
        print("Erro.")

