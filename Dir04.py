# Dir04 - Lista arquivos em um diretório e altera as extensões destes arquivos.
# Autor: Leonardo Antunes dos Santos

import os 

def ChangeFilesExtension(dir, extension):
    for item in os.listdir(dir):
        if ("eadme" in item):
            next
        elif (extension in item):
            next
        else:
            os.rename(''+dir+'/'+item, ''+dir+'/'+item+extension)

extension = input("Digite a extensão do arquivo (ex: .jpg, .png, .gif): ")

dir = r"C:/Users/feoxp7/Downloads/yalefaces/yalefaces"
ChangeFilesExtension(dir, extension)