# Codigo_IP_16 - DeepLearning course - Convolução feita manualmente.

from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2
import os

#Função que fará a convolução de imagens e kernels
def convolve(img, kernel):

    #Dimensões da imagem 
    (iH, iW) = img.shape[:2]
    #Dimensões do kernel
    (kH, kW) = kernel.shape[:2]

    #alocar memória para imagem de saída tomando 
    #cuidado para preencher as bordas da imagem 
    #de entrada para que o tamanho da imagem não 
    #seja reduzido. 
    pad = (kW - 1) // 2
    img = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float32")

    #Loop sobre a imagem de entrada, passando o kernel sobre cada coordenada
    #(x,y) da esquerda para a direita de cima para baixo. 
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            #Extrai a região de interesse da imgem extraindo a região central
            #das dimensões atuais
            roi = img[y - pad:y+pad+1, x-pad:x+pad+1]

            #realiza a convolução 
            k = (roi * kernel).sum()

            output[y - pad, x - pad] = k

    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")
    return output

#Kernels
smallBlur = np.ones((7,7), dtype="float") * (1.0/(7*7))
largeBlur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))
laplacian = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype="int")
sobelX = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype="int")
sobelY = np.array((
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]), dtype="int")

#Acessando diretório com imagem
os.chdir("Miscelanias/Imagens")

#Leitura de imagem
img = cv2.imread('pout.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
convoleOutput = convolve(gray,sobelX)
convoleOutput2 = convolve(gray,sobelY)

#loop para exibição de imagens
while True:
    cv2.imshow('frame',gray)
    cv2.imshow('sobelX',convoleOutput)      
    cv2.imshow('sobelY',convoleOutput2)      

    k = cv2.waitKey(0) & 0xFF     
    if k == 27: break             # ESC key to exit
cv2.destroyAllWindows()