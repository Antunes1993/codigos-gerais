#Montagem Imagens com OpenCV
import os
import cv2
import glob
import random
from imutils import paths
from imutils import build_montages

#Diretorio com imagens
pathRef = "/home/leonardo/Projetos/Projetos/codigos-gerais/Miscelanias/Imagens"
os.chdir(pathRef)

#Lista que irá abrigar as imagens
images = []

#Adiciona cada imagem localizada no diretório na lista de imagens.
os.chdir(pathRef)
for file in glob.glob("*.png"):
    img = cv2.imread(file)
    images.append(img)

#Cria a montagem
montages =build_montages(images, (200,196),(2,2))

#Exibe a montagem
for montage in montages:
    cv2.imshow("Montagem", montage)
    cv2.waitKey(0)