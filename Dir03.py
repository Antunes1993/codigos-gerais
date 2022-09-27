# Dir03 - Gerar CSV a partir de um determinado conjunto de diretorios.
# Autor: Leonardo Antunes dos Santos
import os 
import re
import csv
import shutil

diretorio1 = r"C:\Users\feoxp7\Desktop\SCRIPTS\Scripts_Python\Ambiente_de_testes\armazenamento de arquivos"
diretorio2 = r"C:\Users\feoxp7\Desktop\SCRIPTS\Scripts_Python\Ambiente_de_testes"

def criar_csv(param1, param2):
    os.chdir(param2)
    file = open("registro_de_diretorios","w")
    file2 = open("registro_de_diretorios.csv","w")
    for root, dirs, files in os.walk(param1):
        for filename in files:
            #print(root)
            #print(filename)
            row = (root+'\\'+ filename)
            file.write(str(root.upper())+'\\'+str(filename.upper())+'\n')
            file2.write(str(root.upper())+'\\'+str(filename.upper())+'\n')
    
    file.close()
    file2.close()
                        

criar_csv(diretorio1,diretorio2)