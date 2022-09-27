#Detecção de formatos e de cores [Com problemas]
'''
Este código poderá ser usado para rotular e identificar o 
formato e as cores de figuras em uma imagem a partir das
suas propriedades de contorno. 
'''

'''
Neste código será demonstrado como podemos trabalhar com
o espaço de cores L*a*b junto com a distância Euclidiana 
para taguear, rotular e determinar a cor de objetos em 
imagens. 
'''

import os 
import cv2
import imutils  
import numpy as np
from collections import OrderedDict
from scipy.spatial import distance as dist 

#As classes foram declaradas dentro do código principal pois esse código tem propósitos apenas instrutivos.

#Detecção de formas
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

#Detecção de cores
class ColorDetector:
    def __init__(self):
        #Inicializa um dicionário com as cores vermelho, verde e azul. 
        #O dicionário conterá o nome das cores e os respectivos valores considerando o canal de cor RGB.
        colors = OrderedDict({
            "red":(255,0,0),
            "green":(0,255,0),
            "blue":(0,0,255)})
            
         #Alocação de memória para a imagem L*a*b e inicialização da lista com nome de cores.
        self.lab = np.zeros((len(colors), 1, 3), dtype="uint8")
        self.colorNames = []

        #Loop sobre o dicionario de cores
        for (i, (name, rgb)) in enumerate(colors.items()):
            # Atuaiza o array L*a*b e a lista de nomes. 
            self.lab[i] = rgb
            self.colorNames.append(name)

        # Converte o array L*a*b do espaço de cores RGB para L*a*b
        self.lab = cv2.cvtColor(self.lab, cv2.COLOR_RGB2LAB)


		colors = OrderedDict({
			"red": (255, 0, 0),
			"green": (0, 255, 0),
			"blue": (0, 0, 255)})
		# allocate memory for the L*a*b* image, then initialize
		# the color names list
		self.lab = np.zeros((len(colors), 1, 3), dtype="uint8")
		self.colorNames = []
		# loop over the colors dictionary
		for (i, (name, rgb)) in enumerate(colors.items()):
			# update the L*a*b* array and the color names list
			self.lab[i] = rgb
			self.colorNames.append(name)
		# convert the L*a*b* array from the RGB color space
		# to L*a*b*
		self.lab = cv2.cvtColor(self.lab, cv2.COLOR_RGB2LAB)


    def label(self, image, c):
        #Criar uma máscara para o contorno, então computar o valor da média L*a*b para a região com a
        #máscara.
        mask = np.zeros(img.shape[:2], dtype="uint8")
        cv2.drawContours(mask, [c], -1,255,-1)
        mask = cv2.erode(mask, None, iterations=2)
        mean = cv2.mean(image, mask=mask)[:3]
		
        #Inicializa uma distância mínima
        minDist = (np.inf, None)

        #Loop sobre os valores de L*a*b
        for (i, row) in enumerate(self.lab):

            #Computar a distância entre os valores de cor atuais e a média da imagem (considerando o espaço 
            # de cores L*a*b)
            d = dist.euclidean(row[0], mean)
            #Se a distância for menor que a distância atual, então atualiza a variável de referência. 
            if d < minDist[0]:
                minDist = (d, i)
        #Retorna o nome e a cor que apresentou a menor distãncia.
        return self.colorNames[minDist[1]]

'''
Então porque usamos L*a*b em vez de RGB ou HSV?
Com intuito de real,emte rotular as regiões de uma imagem que contém uma certa cor, nós iremos 
computar a distância Euclidiana entre as nossas cores conhecidas (que estão no array Lab) e as
médias de uma região da imagem em particular.

A cor conhecida que minimizar a distância Euclidiana irá ser escolhida como a cor de identificação. 

E, ao contrário dos espaços de cores HSV e RGB, a distância euclidiana entre as cores L * a * b * 
tem um significado perceptivo real - portanto, vamos usá-la no restante deste post.
'''


#Acessa o diretório com a imagem
os.chdir("/home/leonardo/Projetos/Projetos/codigos-gerais/Miscelanias/Imagens")

#Carregamento e pré-processamento da imagem
img = cv2.imread('shapes_and_colors.jpg')
resized = imutils.resize(img, width=300)
ratio = img.shape[0]/float(resized.shape[0])

blurred = cv2.GaussianBlur(resized, (5, 5), 0)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]

#Detectando contornos
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

#Instanciando a classe ShapeDetector
sd = ShapeDetector()
cl = ColorDetector()


#Identificando cada contorno
for c in cnts:
    try:
        # Computando o centro do contorno e, então, detectando o nome
        # da forma usando apenas o contorno.
        M = cv2.moments(c)
        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)
        shape = sd.detect(c)
        cor = cl.label(lab, c)

        # Multiplicando as coordenadas do contorno pelo ratio e então 
        # desenhando os contornos e o nome da forma na imagem. 
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
        cv2.putText(img, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
        cv2.imshow("Imagem", img)
        cv2.waitKey(0)
    except Exception as error: 
        print(error)

