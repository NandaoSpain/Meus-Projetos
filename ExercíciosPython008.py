print('-' * 50)
print('{:^50}'.format('Listagem de Preços'))
print('-' * 50)
lista = ('Livro', 29.90, 'Celular', 3499.99, 'Travesseiro', 29.90,
         'Computador', 7879.99, 'Garrafa', 165.80, 'Colchão', 2997.99,
         'Guarda Roupa', 1700, 'Ar Condicionado', 1782, 'Cuia', 5.99)
for i, v in enumerate(lista):
    if i % 2 == 0:
        print('{:.<40}'.format(v), end='')
    if i % 2 == 1:
        print('R${:>8.2f}'.format(v))
print('-' * 50)
