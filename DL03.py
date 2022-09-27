# Codigo_DL03 - DeepLearning course - classificador de imagens de cães, gatos e pandas.

#Importando módulos necessários
import os 
import cv2
import pickle
import glob
import numpy as np
import tensorflow as tf 
import matplotlib.pyplot as plt

from imutils import paths
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.models import load_model 

#Instanciando parâmetros e vetores
imgSize = 32
trainingArray = []
labels = []

#Dados separados
trainX = []
trainY = []
testX = []
testY = []

#Labels
Categories=["dogs","cats", "panda"]
#Caminhos utilizados
path="/home/leonardo/Downloads/keras-tutorial/animals"
path2 = "/home/leonardo/Projetos/Projetos/codigos-gerais/Miscelanias/ModelosDeepLearning/Rotulos"
path3 =  "/home/leonardo/Projetos/Projetos/codigos-gerais/Miscelanias/ModelosDeepLearning"
path4 = "/home/leonardo/Downloads/keras-tutorial/images"

def DataCreation(path,path2, imgSize, Categories, trainingArray, labels):
    print ("1. Processo de criação de dados inicializado...")
    i=0
    #Para cada item no vetor Categories será montado um path usando os.path.join
    for categoria in Categories:
        #Acessa cada diretório contendo imagens de cachorros, gatos e pandas.
        os.chdir(os.path.join(path,categoria)) 
        #Transforma as categorias ("dogs", "cats" e "pandas" em números a partir de seu index (0,1,2))
        classLabel = Categories.index(categoria)
        
        print("     Diretório sendo acessado: ", os.path.join(path,categoria))
        #Itera sobre todas as imagens do diretório.
        for item in glob.glob("*.jpg"):
            #Lê a imagem
            img = cv2.imread(item)
            #Redimensiona a imagem e achata os canais da imagem em 1 dimensão.
            imgResized = cv2.resize(img,(imgSize,imgSize)).flatten()
            #Adiciona a imagem achatada ao vetor de treinamento
            trainingArray.append(imgResized) 
            #Adiciona a categoria ao vetor de rótulos
            labels.append(categoria)
            i+=1

    #Normaliza os elementos do vetor de treinamento para que os valores fiquem dentro do intervalo [0,1]
    trainingArray = np.array(trainingArray, dtype="float") / 255.0
    #Transforma o vetor de labels em um vetor numpy
    labels = np.array(labels)

    #Divide os conjuntos de treinamento e teste
    (trainX, testX, trainY, testY) = train_test_split(trainingArray, labels, test_size=0.25, random_state=42)

    #Hot encoding do vetor de rótulos (trainY e testY). 
    #dogs  --> [1,0,0]
    #cats  --> [0,1,0]
    #panda --> [0,0,1]
    lb = LabelBinarizer()
    trainY = lb.fit_transform(trainY)
    testY = lb.fit_transform(testY)
    
    os.chdir(path2)
    f = open("Labels","wb")
    f.write(pickle.dumps(lb))
    f.close()
    print("Processo de criação de dados finalizado...")
    return trainX, trainY, testX, testY, lb

def ModelCreation(trainX, trainY, testX, testY, lb, path):
    #Criação da rede neural
    model = Sequential()
    model.add(Dense(1024, input_shape=(3072,), activation="sigmoid"))
    model.add(Dense(512, activation="sigmoid"))
    model.add(Dense(512, activation="sigmoid"))
    model.add(Dense(len(lb.classes_), activation="softmax"))

    INIT_LR = 0.01
    EPOCHS = 100
    
    print("Treinando a rede neural")
    opt = SGD(lr=INIT_LR)
    #Compilando o modelo     
    model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
    H = model.fit(x=trainX, y=trainY, validation_data=(testX, testY),epochs=EPOCHS, batch_size=32)
    
    #Avaliando a rede neural 
    print("Avaliando a rede neural")
    predictions = model.predict(x=testX, batch_size=32)

    print(classification_report(testY.argmax(axis=1),predictions.argmax(axis=1), target_names=lb.classes_))
    # plot the training loss and accuracy
    N = np.arange(0, EPOCHS)
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(N, H.history["loss"], label="train_loss")
    plt.plot(N, H.history["val_loss"], label="val_loss")
    plt.plot(N, H.history["accuracy"], label="train_acc")
    plt.plot(N, H.history["val_accuracy"], label="val_acc")
    plt.title("Training Loss and Accuracy (Simple NN)")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend()
    model.save(path)
    return model

def TestModel(path2, path3, path4):   
    os.chdir(path2)
    file = open("/home/leonardo/Projetos/Projetos/codigos-gerais/Miscelanias/ModelosDeepLearning/Rotulos/Labels",'rb')
    lb = pickle.load(file)
    
    os.chdir(path3)
    model = load_model(path3)

    os.chdir(path4)
    for item in glob.glob("*.jpg"):
        img = cv2.imread(item)
        output = img.copy()
        img = cv2.resize(img, (imgSize,imgSize))
        image = img.astype("float") / 255.0
        image = image.flatten()
        image = image.reshape((1, image.shape[0]))


        preds = model.predict(image)
        i = preds.argmax(axis=1)[0]
        label = lb.classes_[i]
        
        text = "{}: {:.2f}%".format(label, preds[0][i] * 100)
        cv2.putText(output, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
            (0, 0, 255), 2)

        cv2.imshow("Image", output)
        cv2.waitKey(0)

trainX, trainY, testX, testY, lb = DataCreation(path, path2, imgSize, Categories, trainingArray, labels)
TestModel(path2,path3,path4)