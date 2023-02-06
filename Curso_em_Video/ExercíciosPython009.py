print()
lista = ('Livro', 'Celular', 'Travesseiro', 'Computador', 'Garrafa',
         'Colchao', 'Guarda Roupa', 'Ar Condicionado', 'Cuia')
print(f'Nossa lista de produtos é: ', end='')
for c in lista:
    print(c, end=', ')
print()
for c in lista:
    print(f'\nNa Palavra {c.upper()} temos ', end='')
    for pos, v in enumerate(c):
        if v in 'aeiouAEIOU':
            print(v, end=' ')
print()
