lista = []
pares = []
impares = []
n = 0
while True:
    n = (int(input('Digite um número: ')))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = str(input('Continuamos? [S/N]: ')).strip().upper()[0]
    if resp not in 'S':
        break
print('-' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
