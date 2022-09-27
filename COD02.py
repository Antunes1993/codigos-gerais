#Mecanismo de uma Rede neural simples (1 camada oculta. 2 neurônios.)
import numpy as np 

I1 = 16
I2 = 10
S1_real = 20

#Feedfoward
peso_i11 = 0.9
peso_i12 = 0.2

peso_i21 = 0.2
peso_i22 = 0.5

peso_o11 = 0.1
peso_o21 = 0.2

O1 = (I1*peso_i11) + (I2*peso_i21)
O2 = (I1*peso_i12) + (I2*peso_i22)

S1_calculado = (O1*peso_o11) + (O2*peso_o21)
erro = S1_real - S1_calculado 

print("\nResultado calculado")
print(round(S1_calculado,2))

print("\nErro calculado")
print(round(erro,2))

#BackPropagation
erro_O1 = erro * (peso_o11/(peso_o11+peso_o21))
erro_O2 = erro * (peso_o21/(peso_o11+peso_o21))

erro_I11 = erro_O1 * (peso_i11/(peso_i11+peso_i21))
erro_I21 = erro_O1 * (peso_i21/(peso_i11+peso_i21))

erro_I12 = erro_O2 * (peso_i12/(peso_i12+peso_i22))
erro_I22 = erro_O2 * (peso_i22/(peso_i12+peso_i22))

print("\nErros Entrada 1")
print(round(erro_I11,2))
print(round(erro_I12,2))
print("\nErros Entrada 2")
print(round(erro_I21,2))
print(round(erro_I22,2))
