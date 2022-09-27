# WA02 - API Web para Deteccao aproximada de dados meteorologicos.
# Autor: Leonardo Antunes dos Santos
import os
import sys
import json
import requests as rq

def requisicao(param):
    try:
        req = None
        cidade = param
        req = rq.get('https://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=29a246b1b59f2718d4e4c81c23a8e5a9')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('erro')

def print_info(param):
    dicionario = param
    try:
        print()
        temperatura_celsius = round(((float(dicionario['main']['temp']))-273),2)
        humidade = round(float(dicionario['main']['humidity']),2)
        req = rq.get('https://translate.yandex.net/api/v1.5/tr.json/translate?lang=en-pt&text='+dicionario['weather'][0]['description']+'&key=trnsl.1.1.20200105T043238Z.d400562603b24093.9aefbbe8ad60a2d64590071fc433f84d2d19a020')
        dicionario_clima = json.loads(req.text)
        clima = (dicionario_clima['text'][0])
        print ('Cidade: ', dicionario['name'])
        print ('Temperatura: ',temperatura_celsius,'°C')
        print ('Humidade:', humidade,'%')
        print ('Clima: ', clima)
        print()
    except:
        print("Local nao encontrado")

sair = False
while not sair:
    user = input('Digite o nome da cidade que deseja consultar: ')
    if user == 'SAIR':
        sair = True
    else:
        dicionario = requisicao(user)
        print_info(dicionario)