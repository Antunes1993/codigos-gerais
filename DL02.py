#Noções básicas de ML com Keras
#Treine sua primeira rede neural: classificação básica.

#Classificação de imagens de roupas


#TensorFlow e tf.Keras
import tensorflow as tf
from tensorflow import keras

#Bibliotecas auxiliares
import numpy as np 
import matplotlib.pyplot as plt 
print (tf.__version__)


fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

'''
Labels: 
0	Camisetas/Top (T-shirt/top)
1	Calça (Trouser)
2	Suéter (Pullover)
3	Vestidos (Dress)
4	Casaco (Coat)
5	Sandálias (Sandal)
6	Camisas (Shirt)
7	Tênis (Sneaker)
8	Bolsa (Bag)
9	Botas (Ankle boot)
'''
labels_names = ['Camisetas', 'Calca', 'Suéter', 'Vestidos','Casaco', 'Sandálias', 'Camisas', 'Tênis', 'Bolsa', 'Botas']

#Dados dos conjuntos de treinamento e teste
print (train_images.shape)
print (len(train_labels))
print (test_images.shape)
print (len(test_labels))

#Dados pré-processados
plt.figure()
plt.imshow(train_images[8])
plt.colorbar()
plt.grid(False)
plt.show()

#Escalando as imagens - Para os valores ficarem entre 0 e 1
train_images = train_images / 255.0
test_images = test_images / 255.0

#Plotando 25 figuras
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(labels_names[train_labels[i]])
plt.show()

#Montando a rede neural - Configurando as camadas do modelo e compilando o modelo 

'''
Depois dos pixels serem achatados, a rede consite de uma sequência de duas camadas 
tf.keras.layers.Dense. Essa são camadas neurais densely connected, ou fully connected.
A primeira camada Dense tem 128 nós (ou neurônios). A segunda (e última) camda é uma
softmax de 10 nós que retorna um array de 10 probabilidades, cuja soma resulta em 1.
Cada nó contem um valor que indica a probabilidade de que aquela imagem pertence a 
uma das 10 classes.
'''

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),   #Transforma um array bidimensional em um unidimensional
     keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])


#Compilando o modelo
'''
Antes do modelo estar pronto para o treinamento, é necessário algumas configurações a mais.
Essas serão adicionadas no passo de compilação:

Função Loss —Essa mede quão precisa o modelo é durante o treinamento. Queremos minimizar a função para 
guiar o modelo para direção certa.

Optimizer —Isso é como o modelo se atualiza com base no dado que ele vê e sua função loss.

Métricas —usadas para monitorar os passos de treinamento e teste. O exemplo abaixo usa a acurácia, a 
fração das imagens que foram classificadas corretamente.
'''
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#Treinando o modelo
model.fit(train_images, train_labels, epochs=10)

#Medição de acurácia
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTeste acuracia:', test_acc)

#Realizando predições
predictions = model.predict(test_images)

#A predição é um array de 10 números, indicando a chance daquela amostra pertencer a cada uma das 10 classes
#de roupa. O número que for maior, indica a classe com maior chance da roupa pertencer.
print (predictions[0])

#Identificando o maior número no array de predição
print(np.argmax(predictions[0]))


#Podemos mostrar graficamente como se parece em um conjunto total de previsão de 10 classes.
def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(labels_names[predicted_label],
                                100*np.max(predictions_array),
                                labels_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')


#Vamos olhar a previsão imagem na posição 0, do array de predição.
i = 0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels)
plt.show()

#Vamos olhar a previsão imagem na posição 12, do array de predição.
i = 12
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels)
plt.show()

# Plota o primeiro X test images, e as labels preditas, e as labels verdadeiras.
# Colore as predições corretas de azul e as incorretas de vermelho.
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions, test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions, test_labels)
plt.show()