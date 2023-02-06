print('-' * 30)
print('LOJAS SUPER BARATÃO')
print('-' * 30)
total = caro = barato = cont = 0
baratonome = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço do Produto: R$'))
    total += preço
    cont += 1
    if cont == 1:
        barato = preço
        baratonome = produto
    elif preço < barato:
        barato = preço
        baratonome = produto
    elif preço >= 1000:
        caro += 1
    resp = ' '
    while resp not in 'S':
        resp = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]
    if resp not in 'S':
        break
print(f'O total da compra foi R${total}')
print(f'Temos {caro} produto custando mais que R$1.000,00')
print(f'O produto mais barato foi {baratonome} que custa R${barato}')
