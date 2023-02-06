lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp not in 'S':
        break
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
if 5 in lista:
    print('A lista contém o valor 5.')
else:
    print('O valor 5 não foi encontrado na lista!')
