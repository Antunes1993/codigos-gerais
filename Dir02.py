# Dir02 - Copia todos os arquivos de uma estrutura de diretorios para um diretorio especifico.
# Autor - Leonardo Antunes dos Santos
import os
import shutil

print ("\n-----------------------------------------------------------------------------------------------------")
print ("\nEste código irá copiar os arquivos de pastas e subpastas localizados dentro de um diretório raiz \npara um diretório de destino de escolha do usuário.")
print ("\n-----------------------------------------------------------------------------------------------------")
dir1 = input ("Insira o caminho da pasta de origem raiz: ")
dir2 = input ("Insira o caminho da pasta de destino: ")

def copiar_arquivos(dir_origem,dir_destino):
    for root, dirs, files in os.walk(dir_origem):
        for item in files:
            print (item)
            os.chdir (root)
            shutil.copy2(item,dir_destino)
    
copiar_arquivos(dir1,dir2)

