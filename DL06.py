from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras import backend as K

class LeNet:
    @staticmethod
    def build(width, height, depth, classes):
        model = Sequential()
        inputShape = (height, width, depth)

        if (K.image_data_format() == "channels_first"):
            inputShape = (depth, height, width)

        #Primeira camada - Conv --> Relu --> Pool
        model.add(Conv2D(20,(5,5), padding="same",input_shape=inputShape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2,2), strides=(1,1)))

        #Segunda camada - Conv --> Relu --> Pool
        model.add(Conv2D(50,(5,5), padding="same",input_shape=inputShape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2,2), strides=(1,1)))

        # Camada FC => RELU
        '''
        Pegamos o resultado da camada anterior e transformamos em um unico vetor. 
        Dessa forma, poderemos aplicar as camadas conectadas.
        '''
        model.add(Flatten())
        #Camada com 500 neurônios, ativados pela função Relu. 
        model.add(Dense(500))
        model.add(Activation("relu"))

		# Classificador softmax
        '''
        Definimos outra camada totalmente conectada (camada FC - Fully Connected), porém 
        essa contem apenas 2 neurônios (classes que queremos reconhecer).
        A camada será alimentará o classificador softmax que apresentará a probabilidade 
        da imagem pertencer a cada classe.
        '''
        model.add(Dense(classes))
        model.add(Activation("softmax"))
		
        return model    