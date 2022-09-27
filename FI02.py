import os
import csv
import numpy as np
import xlsxwriter

import pandas as pd 
import matplotlib.pyplot as plt

diretorio1 = r"C:\Users\feoxp7\Desktop\SCRIPTS\Codigos_Python\codigos-gerais\MODULO FINANCAS"
os.chdir(diretorio1)
workbook = xlsxwriter.workbook('Acoes.xlsx')
worksheet = workbook.add_worksheet()

with open('statusinvest-busca-avancada.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        print(row[1])

