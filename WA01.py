# WA01 - API WEB exibir endereco a partir do CEP.
# Autor: Leonardo Antunes dos Santos
import os
import sys
import json
import requests as rq

req = None
def requisicao(param):
    try: 
        req = rq.get('https://api.postmon.com.br/v1/cep/'+ param)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        None
        

def print_info(cep):
    try:
        print()
        print('Cidade:',cep['cidade'])
        print('Bairro:',cep['bairro'])
        print('Logradouro:', cep['logradouro'])
        print()
    except:
        print("CEP informado nao exsite.")

sair = False
while not sair:
    op = input ('Escreva o CEP que deseja consultar:')
    if op == 'SAIR':
        sair = True
    else:
        pesquisa = requisicao(op)
        print_info(pesquisa)
        
