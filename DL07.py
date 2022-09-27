#Treinando uma rede neural 
import matplotlib
matplotlib.use("Agg") #Permite que salvemos o gráfico no disco.

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelBinarizer

import DL06 as NeuralnetReference
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import glob
import cv2
import os

#Dados iniciais
EPOCHS = 25
INIT_LR = 1e-3
BS = 32
imgSize = 28
#Vetores de dados
trainingArray = []
labels = []

#Labels
Categories=["dogs","cats", "panda"]

#Caminhos utilizados
path="/home/leonardo/Downloads/keras-tutorial/animals"
path2 = "/home/leonardo/Projetos/Projetos/codigos-gerais/Miscelanias/ModelosDeepLearning/Rotulos"
path3 =  "/home/leonardo/Projetos/Projetos/codigos-gerais/Miscelanias/ModelosDeepLearning"
path4 = "/home/leonardo/Downloads/keras-tutorial/images"

print("Iniciando o carregamento de imagens.")
#Para cada item no vetor Categories será montado um path usando os.path.join
for categoria in Categories:
    #Acessa cada diretório contendo imagens.
    os.chdir(os.path.join(path,categoria)) 
    #Transforma as categorias em números a partir de seu index.
    classLabel = Categories.index(categoria)
    
    print("  Diretório sendo acessado: ", os.path.join(path,categoria))
    #Itera sobre todas as imagens do diretório.
    for item in glob.glob("*.jpg"):
        #Lê a imagem
        img = cv2.imread(item)
        #Redimensiona a imagem e achata os canais da imagem em 1 dimensão.
        imgResized = cv2.resize(img,(imgSize,imgSize))
        #imgResized = img_to_array(img)
        #Adiciona a imagem achatada ao vetor de treinamento
        trainingArray.append(imgResized) 
        #Adiciona a categoria ao vetor de rótulos
        labels.append(categoria)

#Normaliza os elementos do vetor de treinamento para que os valores fiquem dentro do intervalo [0,1]
trainingArray = np.array(trainingArray, dtype="float") / 255.0
#Transforma o vetor de labels em um vetor numpy
labels = np.array(labels)

#Divide os conjuntos de treinamento e teste
(trainX, testX, trainY, testY) = train_test_split(trainingArray, labels, test_size=0.25, random_state=42)

#Hot encoding do vetor de rótulos (trainY e testY). 

lb = LabelBinarizer()
trainY = lb.fit_transform(trainY)
testY = lb.fit_transform(testY)

aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
	height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
	horizontal_flip=True, fill_mode="nearest")

model = NeuralnetReference.LeNet.build(width=28, height=28, depth=3, classes=2)
opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
model.compile(loss="binary_crossentropy", optimizer=opt,
	metrics=["accuracy"])

H = model.fit(x=aug.flow(trainX, trainY, batch_size=BS),
	validation_data=(testX, testY), steps_per_epoch=len(trainX) // BS,
	epochs=EPOCHS, verbose=1)


print("[INFO] serializing network...")
model.save(args["model"], save_format="h5")