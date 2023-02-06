pessoas = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()

    resp = str(input('Continuamos? ')).strip().upper()[0]
    if resp in 'N':
        break
print()
print(f'Ao todo foram cadastrados {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior} kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso foi de {menor} kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')
print()
