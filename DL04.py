# Codigo_DL04 - DeepLearning course - Coletar imagens do google para montar um dataset

from imutils import paths
import requests
import cv2 
import os 
import shutil
import glob 

path = "/home/leonardo/Projetos/Projetos/codigos-gerais/Miscelanias/ArquivosReferencia"
pathOutput = "/home/leonardo/Downloads/DataSetCreated/Outros"

os.chdir(path)
file = open("urls.txt")
rows = file.read().strip().split("\n")
total = 0

os.chdir(pathOutput)

for row in rows:   
    try:
        if (".jpg") in row:        
            url = row
            response = requests.get(url, stream=True)
            imgName = ("{}.jpg".format(str(total).zfill(8))) 
            print ("Baixando imagem...: ",imgName)
            with open(imgName, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            total += 1  
        elif(".png") in row: 
            url = row
            response = requests.get(url, stream=True)
            imgName = ("{}.png".format(str(total).zfill(8))) 
            print ("Baixando imagem...: ",imgName)
            with open(imgName, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            total += 1  
        elif(".jpeg") in row: 
            url = row
            response = requests.get(url, stream=True)
            imgName = ("{}.png".format(str(total).zfill(8))) 
            print ("Baixando imagem...: ",imgName)
            with open(imgName, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            total += 1  
    except:
        print("Não foi possível baixar essa imagem.")
print ("Download finalizado.") 


for item in glob.glob("*.jpg"):
    try:
        #Leitura de imagem
        img = cv2.imread(item)
        #Conversão RGB -> Grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #Imagem normal e imagem equalizada
        #cv2.imshow(gray, img)
    except:
        os.remove(item)
        print("item removido: ", item)
        continue
for item in glob.glob("*.png"):
        try:
            #Leitura de imagem
            img = cv2.imread(item)
            #Conversão RGB -> Grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #Imagem normal e imagem equalizada
            #cv2.imshow(gray, img)
        except:
            os.remove(item)
            print("item removido: ", item)
            continue
for item in glob.glob("*.jpeg"):
        try:
            #Leitura de imagem
            img = cv2.imread(item)
            #Conversão RGB -> Grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #Imagem normal e imagem equalizada
            #cv2.imshow(gray, img)
        except:
            os.remove(item)
            print("item removido: ", item)
            continue
