# Codigo_DL05 - DeepLearning course - Keras 2D e camadas convolucionais.

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense
from tensorflow.keras import backend as K
from tensorflow.keras.optimizers import SGD
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import pickle
import glob
import cv2
import os


#Instanciando parâmetros e vetores
imgSize = 32
epochs = 100

trainingArray = []
labels = []

#Dados separados
trainX = []
trainY = []
testX = []
testY = []

#Labels
Categories = ["Faces", "Leopards", "Motorbikes", "airplanes"]
pathInputRoot ="/home/leonardo/Downloads/101_ObjectCategories"
pathLabels = "/home/leonardo/Projetos/Projetos/codigos-gerais/Miscelanias/ModelosDeepLearning/Rotulos"
pathModel =  "/home/leonardo/Projetos/Projetos/codigos-gerais/Miscelanias/ModelosDeepLearning"
pathTestImages = "/home/leonardo/Downloads/101_ObjectCategories/TESTE_REDES"

class StridedNet:
    @staticmethod
    def build(width, height, depth, classes, reg, init="he_normal"):
        model = Sequential()
        inputShape = (height, width, depth)
        chanDim = -1
        
        if K.image_data_format() == "channels_first":
            inputShape = (depth, height, width)
            chanDim = 1

        #camada 1
        model.add(Conv2D(16, (7, 7), strides=(2, 2), padding="valid",
            kernel_initializer=init, kernel_regularizer=reg,
            input_shape=inputShape))
        
        model.add(Conv2D(32, (3, 3), padding="same",
            kernel_initializer=init, kernel_regularizer=reg))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(Conv2D(32, (3, 3), strides=(2, 2), padding="same",
            kernel_initializer=init, kernel_regularizer=reg))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(Dropout(0.25))

        #camada 2
        model.add(Conv2D(64, (3, 3), padding="same",
            kernel_initializer=init, kernel_regularizer=reg))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(Conv2D(64, (3, 3), strides=(2, 2), padding="same",
            kernel_initializer=init, kernel_regularizer=reg))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(Dropout(0.25))
        
        model.add(Conv2D(128, (3, 3), padding="same",
            kernel_initializer=init, kernel_regularizer=reg))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(Conv2D(128, (3, 3), strides=(2, 2), padding="same",
            kernel_initializer=init, kernel_regularizer=reg))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(Dropout(0.25))

        #camada 3
        model.add(Flatten())
        model.add(Dense(512, kernel_initializer=init))
        model.add(Activation("relu"))
        model.add(BatchNormalization())
        model.add(Dropout(0.5))
        # softmax classifier
        model.add(Dense(classes))
        model.add(Activation("softmax"))
        # return the constructed network architecture
        return model

def DataCreation(path, Categories, trainingArray, labels):
    print("1. Processo de criação de dados inicializado...")
    for categoria in Categories:
        os.chdir(os.path.join(path,categoria))
        classLabel = Categories.index(categoria)
        i = 0
        for item in glob.glob("*.jpg"):
            img = cv2.imread(item)
            #Se for usar o segundo modelo, adicionar .flatten()
            imgResized = cv2.resize(img,(imgSize, imgSize)).flatten()
            trainingArray.append(imgResized)
            labels.append(categoria)
            i+=1           
    
    trainingArray = np.array(trainingArray, dtype="float") / 255.0
    labels = np.array(labels)
    (trainX, testX, trainY, testY) = train_test_split(trainingArray, labels, test_size=0.25, random_state=42)
    
    lb = LabelBinarizer()
    trainY = lb.fit_transform(trainY)
    testY = lb.fit_transform(testY)
    
    return trainX, trainY, testX, testY, lb

def ModelCreation(trainX, trainY, testX, testY, lb, epochs):
    #Criação da rede neural
    model = Sequential()
    model.add(Dense(1024, input_shape=(3072,), activation="sigmoid"))
    model.add(Dense(512, activation="sigmoid"))
    model.add(Dense(512, activation="sigmoid"))
    model.add(Dense(len(lb.classes_), activation="softmax"))

    INIT_LR = 0.01
    
    print("Treinando a rede neural")
    opt = SGD(lr=INIT_LR)
    #Compilando o modelo     
    model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
    H = model.fit(x=trainX, y=trainY, validation_data=(testX, testY),epochs=epochs, batch_size=32)
    
    #Avaliando a rede neural 
    print("Avaliando a rede neural")
    predictions = model.predict(x=testX, batch_size=32)

    print(classification_report(testY.argmax(axis=1),predictions.argmax(axis=1), target_names=lb.classes_))
    # plot the training loss and accuracy
    N = np.arange(0, epochs)
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
    #model.save(path)
    return model

def SecondModelCreation(trainX, trainY, testX, testY, lb, epochs):
    aug = ImageDataGenerator(rotation_range=20, zoom_range=0.15,
	width_shift_range=0.2, height_shift_range=0.2, shear_range=0.15,
	horizontal_flip=True, fill_mode="nearest")

    #Inicializando o otimizador e o modelo
    opt = Adam(lr=1e-4, decay=1e-4 / epochs)
    model = StridedNet.build(width=32, height=32, depth=3, classes=len(lb.classes_), reg=l2(0.0005))
    model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
    H = model.fit(x=aug.flow(trainX, trainY, batch_size=32),
        validation_data=(testX, testY), steps_per_epoch=len(trainX) // 32,
        epochs=epochs)

    predictions = model.predict(x=testX, batch_size=32)
    print(classification_report(testY.argmax(axis=1),predictions.argmax(axis=1), target_names=lb.classes_))
    
    N = epochs
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
    plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
    plt.plot(np.arange(0, N), H.history["accuracy"], label="train_acc")
    plt.plot(np.arange(0, N), H.history["val_accuracy"], label="val_acc")
    plt.title("Training Loss and Accuracy on Dataset")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend(loc="lower left")
    #plt.show()
    return model

def TestFirstModel(path, model):   
    os.chdir(path)
    for item in glob.glob("*.jpg"):
        img = cv2.imread(item)
        output = img.copy()
        img = cv2.resize(img, (imgSize,imgSize))
        image = img.astype("float") / 255.0
        image = image.flatten()
        image = image.reshape((1, image.shape[0]))


        preds = model.predict(x=image, batch_size=32)
        i = preds.argmax(axis=1)[0]
        label = lb.classes_[i]
        
        text = "{}: {:.2f}%".format(label, preds[0][i] * 100)
        cv2.putText(output, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
            (0, 0, 255), 2)

        cv2.imshow("Image", output)
        cv2.waitKey(0)

trainX, trainY, testX, testY, lb = DataCreation(pathInputRoot, Categories, trainingArray, labels)
print (" === Dados de entrada === ")
print("Treinamento: ", trainX.shape)
print("Teste: ", testX.shape)

model = ModelCreation(trainX, trainY, testX, testY, lb, epochs)
TestFirstModel(pathTestImages,model)



