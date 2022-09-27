import os
import csv
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

diretorio1 = r"C:\Users\feoxp7\Desktop\SCRIPTS\Codigos_Python\codigos-gerais\MODULO FINANCAS\statusinvest-busca-avancada.csv"
diretorio2 = r"C:\Users\feoxp7\Desktop\SCRIPTS\Codigos_Python\codigos-gerais\MODULO FINANCAS\Investimentos.xlsx"

df = pd.read_csv(diretorio1, delimiter=';')
df = df.fillna(0)

# Dataframe com informações escolhidas
data_df = df[[
# Ticker    
'TICKER', 
# Indicadores de lucratividade
'ROE','ROIC','MARG. LIQUIDA','MARGEM EBIT',   
# Indicadores de preço
'PSR','P/L','P/VP','P/ATIVOS','P/EBIT',
# Indicadores de endividamento
'LIQ. CORRENTE','DIV. LIQ. / PATRI.',
# Indicadores de cre scimento
'CAGR LUCROS 5 ANOS','CAGR RECEITAS 5 ANOS']]

data_df.set_index("TICKER", inplace=True)
data_df = (data_df[data_df["ROE"] > 0])

print(data_df.head(10))

# Limites ROE
data_df = (data_df[data_df["ROE"] <100])
# Limites ROIC
data_df = (data_df[data_df["ROIC"] > 0])
data_df = (data_df[data_df["ROIC"] <100])
# Limites PSR
data_df = (data_df[data_df["PSR"] < 3])
#data_df.to_xlsx(diretorio2)
'''
print("---------------------------------------")
print("ROE Média:", round(data_df["ROE"].mean(),2))
print("ROIC Média:", round(data_df["ROIC"].mean(),2))
print("PSR Média:", round(data_df["PSR"].mean(),2))
print("P/L Média:", round(data_df["P/L"].mean(),2))
print("CAGR Lucro Média:", round(data_df["CAGR LUCROS 5 ANOS"].mean(),2))
'''



'''
Quanto maior esses indicadores, melhor.
EBIT - Earnings Before Interests and tributation - Lucro antes de impostos e tributações
EBITDA - Earnings before interests, tributation, depreciation and amortization 

MARGEM EBIT = (LUCRO / RECEITA LÍQUIDA)
MARGEM BRUTA = (LUCRO / RECEITA BRUTA)

P/EBIT - Tempo em anos que vai levar para fazer em lucro operacional o valor de mercado da empresa.
O valor ideal para o P/EBIT no máximo 10 anos. Quanto menor o P/EBIT melhor. 

PSR é um indicador que relaciona a receita total das vendas geradas pela empresa com o seu valor de
mercado. Em geral as receitas são menos voláteis que o lucro. Assim esse indicador pode ser mais 
confiável que o indicador P/L. Quanto menor o PSR, mais barata estará a empresa. Logo, quanto menor
o PSR, melhor.

Quem popularizou o PSR foi o investidor Kenneth Fisher. Ele propos 3 regras a seguir: 
    1. Evite ações com PSRs maior que 1.5 e nunca compre ações com PSR maior que 3.
    2. Procure por companhias com PSR menores que 1.00. Ações com PSR de 0.75 estariam com bom desconto
        de preço.
    3. Venda os papéis de qualquer companhia se seu PSR estiver entre 3.0 e 6.0.
'''