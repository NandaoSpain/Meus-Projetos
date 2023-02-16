def ParImpar(num):
    if num % 2 == 0:
        print(f'O número {num} é Par')
    else:
        print(f'O número {num} é Ímpar')


resultado = ParImpar(int(input('Digite um número')))
