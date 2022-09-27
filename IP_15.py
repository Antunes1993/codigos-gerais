#Gravando vídeos com OpenCV em 4 frames coloridos. 

import os 
import cv2
import imutils
import numpy as np

def VideoOpenCV():
    #Carrega câmera
    capture = cv2.VideoCapture(0)

    #Inicializa as variáveis de gravação
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    writer = None
    (height, width) = (None, None)
    zeros = None

    #Loop para exibição de imagens
    while 1:
        #Criação dos frames
        ret, img = capture.read()
   
        #Verifica se writer está setado como None
        if writer is None: 
            (h, w) = img.shape[:2]
            writer = cv2.VideoWriter('output.avi', fourcc, 10, (w * 2, h * 2), True)
            zeros = np.zeros((h, w), dtype="uint8")

        #Separa a imagem em componentes RGB e, então, constrói uma representação RGB para cada frame individualmente.
        (B, G, R) = cv2.split(img)
        R = cv2.merge([zeros, zeros, R])
        G = cv2.merge([zeros, G, zeros])
        B = cv2.merge([B, zeros, zeros])
        
        #Constrói o frame final colocando cada componente lado a lado. 
        output = np.zeros((h * 2, w * 2, 3), dtype="uint8")
        output[0:h, 0:w] = img
        output[0:h, w:w * 2] = R
        output[h:h * 2, w:w * 2] = G
        output[h:h * 2, 0:w] = B

        #Grava o video
        writer.write(output)

        #Exibe os frames
        cv2.imshow("Frame", output)

        #Se pressionar letra 'q', interrompe a filmagem
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()
    writer.release()


VideoOpenCV()
