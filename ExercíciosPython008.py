print('-' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-' * 50)
lista = ('Livro', 29.90, 'Celular', 3499.99, 'Travesseiro', 29.90,
         'Computador', 7879.99, 'Garrafa', 165.80, 'Colchão', 2997.99,
         'Guarda Roupa', 1700, 'Ar Condicionado', 1782, 'Cuia', 5.99)
for i, v in enumerate(lista):
    if i % 2 == 0:
        print(f'{v:.<40}', end='')
    if i % 2 == 1:
        print(f'R${v:>8.2f}')
print('-' * 50)