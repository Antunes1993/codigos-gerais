# Dir01 - Cria estrutura de diretorios a partir de um CSV.
# Autor: Leonardo Antunes dos Santos
import os
import re
import csv
import sys
import shutil

dir1 = r"C:\Users\feoxp7\Desktop\SCRIPTS\Scripts_Python\Ambiente_de_testes"
dir2 = r"C:\Users\feoxp7\Desktop\SCRIPTS\Scripts_Python\Ambiente_de_testes\criacao_automatica_diretorios"
arquivo = 'Book2.csv'

def cria_diretorio(param1, param2, param3):
    os.chdir(param1)
    with open(param2) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        cont = 0
        path = []

        for item in csv_reader:
            #Trata diretorios com != profundidades.
            for element in item:
                if element == '':
                    item.remove(element)
                else: 
                    None
            
            if cont == 0:
                #Titulo das colunas
                cont += 1
            else:
                path_item = "\\".join(item[:-1])
                path.append(path_item)
        
        for item in path:
            try:
                os.chdir(param3)
                os.makedirs(item)
                print (f"Criado diretorio{item}")
            except Exception as error:
                print ("Diretorio ja existente")       
                print(error)
    return path

path = cria_diretorio(dir1,arquivo,dir2)