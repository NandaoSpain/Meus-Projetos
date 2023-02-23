# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [(l1[i], l2[i]) for i in range(intervalo)]

print(zipper(l1, l2))

#ou

print(list(zip(l1, l2)))

#ou

print(list(zip_longest(l1, l2, fillvalue='Sem Cidade')))