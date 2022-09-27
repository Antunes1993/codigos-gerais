# Codigo_DL01 - DeepLearning course - Hand Written digits classifier.

import numpy as np
import tensorflow as tf 
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist #28x28 images of hand-written digits 0-9
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

plt.imshow(x_train[1], cmap = plt.cm.binary)
plt.show()

model = tf.keras.models.Sequential() #Sequential Model - "Feedfoward model"
model.add(tf.keras.layers.Flatten()) #Input Layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) #Hidden Layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) #Hidden Layer
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax)) #Output Layer

#Compila o modelo
model.compile (optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])
#Treina o modelo
model.fit(x_train,y_train, epochs=3)

#Avalia os resultados
val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

