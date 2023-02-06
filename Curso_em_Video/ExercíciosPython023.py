from random import randint
from time import sleep
jogadores = dict()
jogadores['Jogador-1'] = randint(1, 6)
jogadores['Jogador-2'] = randint(1, 6)
jogadores['Jogador-3'] = randint(1, 6)
jogadores['Jogador-4'] = randint(1, 6)
print()
print('*' * 28)
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado')
    sleep(0.5)
print('*' * 28)
print(f' = Ranking dos Jogadores = ')
cont = 1
for i in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f' {cont}º Lugar: ', end='')
    print(f' {i} com {jogadores[i]}')
    cont += 1
