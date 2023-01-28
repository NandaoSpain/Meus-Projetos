num = [[], [], []]
for c in range(0, 3):
    num[c].append(int(input(f'Digite um valor para [{c}, 0]: '))),
    num[c].append(int(input(f'Digite um valor para [{c}, 1]: '))),
    num[c].append(int(input(f'Digite um valor para [{c}, 2]: ')))
print()
for l in range(0, 3,):
    for c in range(0, 3):
        print(f'[{num[l][c]:^5}]', end='')
    print()
print()
pares = 0
for l in range(0, 3,):
    for c in range(0, 3):
        if num [l][c] % 2 == 0:
            pares += num[l][c]
print(f'A soma dos valores pares é {pares}')
terceira = (num [0][2] + num [1][2] + num [2][2])
print(f'A soma dos valores da terceira coluna é {terceira}')
maiorsegunda = 0
for c in range(0, 3):
    if c == 0:
        maiorsegunda = num[1][c]
    else:
        if num[1][c] > maiorsegunda:
            maiorsegunda = num[1][c]
print(f'O maior valor da segunda linha é {maiorsegunda}')
