def ParImpar(num):
    if num % 2 == 0:
        return f'O número {num} é Par'
    else:
        return f'O número {num} é Ímpar'


print(ParImpar(int(input('Digite um número'))))
