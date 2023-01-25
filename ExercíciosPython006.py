from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for c in num:
    print(c, end=' ')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')
