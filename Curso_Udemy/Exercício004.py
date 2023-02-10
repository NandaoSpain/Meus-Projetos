from time import sleep
while True:
    numero1 = input('Digite um número: ')
    operador = input('Digite o operador: ')
    numero2 = input('Digite outro numero: ')    

    numeros_validos = None
    n1_float = 0
    n2_float = 0

    try:
        n1_float = float(numero1)
        n2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos!')
        continue

    operadores_permitidos = '+-*/'
    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue   
    if len(operador) > 1:
        print('Digite apenas 1 operador')     
        continue
    print('Realizando sua conta...')
    sleep(1)
    print('Resultado abaixo:')
    sleep(1)
    if operador == '+':
        print(f'{n1_float} + {n2_float} =', n1_float + n2_float)
    elif operador == '-':
        print(f'{n1_float} - {n2_float} =', n1_float - n2_float)
    elif operador =='/':
        print(f'{n1_float} / {n2_float} =', n1_float / n2_float)
    elif operador == '*':
        print(f'{n1_float} * {n2_float} =', n1_float * n2_float)
    else:
        print('erro brabo')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        print('Saindo...')
        break
        