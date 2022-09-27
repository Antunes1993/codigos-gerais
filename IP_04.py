#Código para fazer equalização de histogramas de uma imagem.
from matplotlib import pyplot as plt
import numpy as np
import glob
import cv2
import os

pathRef = "C:\\Users\\feoxp7\\Desktop\\TestTesseract" 
#input("Digite o caminho com as imagens que serão analisadas:")
os.chdir(pathRef)

listImages = []
previousImage = []
currentImage = []
flag = 0

for item in glob.glob("*.jpg"):
    listImages.append(item)
for item in glob.glob("*.png"):    
    listImages.append(item)

print ("Digite 'a' para avançar para a próxima imagem e 's' para voltar para a imagem anteior.")
while True:
    userCommand = input("Digite comando: ")
    if (userCommand == "a" and flag == 0):
        currentImage = listImages[flag] 
        flag += 1
        print ("Imagem atual: ",currentImage)
        #print ("Previous: ",previousImage)
        
    elif (userCommand == "a" and flag > 0):
        previousImage = listImages[flag-1]
        currentImage = listImages[flag]
        flag += 1
        print ("Imagem atual: ",currentImage)
        print ("Imagem anterior: ",previousImage)

    elif (userCommand == "s" and flag > 0):
        currentImage = listImages[flag-2]
        previousImage = listImages[flag-3]
        flag -= 1
        print ("Imagem atual: ",currentImage)
        print ("Imagem anterior: ",previousImage)
        print ("flag: ",flag)

    #Leitura de imagem
    img = cv2.imread(currentImage)
    #Conversão RGB -> Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Conversão RGB -> YUV
    yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    #Equalizaçãode Histograma
    yuv[:,:,0] = cv2.equalizeHist(yuv[:,:,0])
    hist_equalization_result = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)

    #Imagem normal e imagem equalizada
    cv2.imshow("Imagem equalizada", hist_equalization_result)
    cv2.imshow("Imagem normal", img)
    
    '''
    #Histogramas
    hist01 = cv2.calcHist([hist_equalization_result],[0],None,[256],[0,256])
    plt.hist(hist_equalization_result.ravel(),256,[0,256])
    plt.title('Histograma imagem equalizada')
    plt.show()

    hist02 = cv2.calcHist([hist_equalization_result],[0],None,[256],[0,256])
    plt.hist(img.ravel(),256,[0,256])
    plt.title('Histograma imagem original')
    plt.show()
    '''
    
    #loop para exibição de imagens
    while True:
        k = cv2.waitKey(0) & 0xFF     
        if k == 27: break             # ESC key to exit
    cv2.destroyAllWindows()
 