from random import sample
from time import sleep
print('-' * 40)
print(f'{"Jogos da Mega Sena Premiada":^40}')
print('-' * 40)
quant = int(input('Quantos jogos devo sortear? '))
print()
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
         21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40,
         41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
for c in range(1, quant + 1):
    sorteio = sorted(sample(lista, 6))
    print(f'Jogo número {c}: {sorteio}')
    sleep(1)
print()
print('-=' * 6, f'< Boa Sorte >', '-=' * 6)
