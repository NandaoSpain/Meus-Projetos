from random import randint
from time import sleep


def sorteia():
    for c in range(0, 5):
        num.append(randint(1, 10))
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in num:
        print(f'{c}', end=' ')
        sleep(0.3)
    print(' PRONTO!')


def somaPar():
    par = 0
    print(f'Somando os valores pares de: ', end=' ')
    for c, v in enumerate(num):
        print(f'{v}', end=' ')
        sleep(0.3)
        if v % 2 == 0:
            par += v
    print(f', Temos: {par}')


num = []
sorteia()
somaPar()
