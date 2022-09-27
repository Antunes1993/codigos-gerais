#Script_OCR01 - Cria um arquivo txt com informações contidas em uma imagem utilizando OCR.
#Autor: Leonardo Antunes dos Santos
import os
import cv2
import pytesseract
from PIL import Image



#path = str(input("Insira o endereco do diretorio onde esta o documento: "))
os.chdir(r"C:\Users\feoxp7\Desktop\PROJETOS\Eldorado\FDs")

text = pytesseract.image_to_string(Image.open('OCR_01.jpg'))
doc_info = open('Informacoes_Documento.txt',"w")
doc_info.write(text)
doc_info.close()