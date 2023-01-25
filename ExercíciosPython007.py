n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
números = (n1, n2, n3, n4)
nove = 0
for c in números:
    if c == 9:
        nove += 1
print(f'Você digitou os valores {números}')
print(f'O valor 9 apareceu {nove} vezes')
if 3 in números:
    tres = (números.index(3) + 1)
    print(f'O valor 3 apareceu na {tres}ª posição')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares digitados foram: ', end='')
for c in números:
    if c % 2 == 0:
        print(c, end=' ')
