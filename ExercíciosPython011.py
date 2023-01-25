lista = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso! ')
    else:
        print('Valor Duplicado, não vou adicionar!')
    resp = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if resp not in 'Ss':
        break
print()
print(f'Você digitou os valores {sorted(lista)}')
