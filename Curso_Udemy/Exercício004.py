while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro numero: ')
    operador = input('Digite o operador: ')

    numeros_validos = None

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
    
    if operador == '+':
        ...
    elif operador == '-':
        ...
    elif operador =='/':
        ...
    elif operador == '*':
        ...
    else:
        print('erro brabo')



    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break
        print('Saindo...')