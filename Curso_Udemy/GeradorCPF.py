import sys
import os
from time import sleep
from random import randint
print('Gerador de CPF'.center(30))
nove_digitos = []
for c in range(9):
    nove_digitos.append(randint(0,9))
multiplicador1 = 10        
resultadosoma1 = 0
for c in nove_digitos:
    resultadosoma1 += c * multiplicador1
    multiplicador1 -= 1 
resultado = resultadosoma1 * 10 % 11
primeiro_digito = resultado if resultado <= 9 else 0
nove_digitos.append(primeiro_digito)
resultadosoma2 = 0
multiplicador2 = 11
for c in nove_digitos:
    resultadosoma2 += c * multiplicador2
    multiplicador2 -= 1
resultado2 = resultadosoma2 * 10 % 11
segundo_digito = resultado2 if resultado2 <=9 else 0
nove_digitos.append(segundo_digito)
print('O CPF Gerado foi ', end='')
print(*nove_digitos, sep='')
