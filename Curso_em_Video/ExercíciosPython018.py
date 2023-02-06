num = [[], [], []]
for c in range(0, 3):
    num[c].append(int(input(f'Digite um valor para [{c}, 0]: '))),
    num[c].append(int(input(f'Digite um valor para [{c}, 1]: '))),
    num[c].append(int(input(f'Digite um valor para [{c}, 2]: ')))

for l in range(0, 3,):
    for c in range(0, 3):
        print(f'[{num[l][c]:^5}]', end='')
    print()
