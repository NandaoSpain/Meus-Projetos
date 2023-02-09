def área(larg, comp):
    a = (larg * comp)
    print(f'A área de um terreno de {larg:.2f}m x {comp:.2f}m é de {a:.2f}m')


print('Controle de Terreno')
print('-' * 20)
l = float(input('Largura (m) :'))
c = float(input('Comprimento (m): '))
área(l, c)
print()
