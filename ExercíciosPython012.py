lista = []
for c in range (0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Valor adicionado ao final lista...')

    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Valor Adicionado na posição {pos}')
                break
            pos += 1
print()
print('*-' * 30)
print(f'Os valores adicionados em ordem foram {lista}')
print('*-' * 30)
