def voto():
    print('-' * 30)
    from datetime import date
    nasc = int(input('Em que ano você nasceu? '))
    idade = date.today().year - nasc
    resultado = ''
    if idade < 16:
        resultado = print(f'Com {idade} anos: Não Vota')
    elif 16 <= idade < 18 or idade > 65:
        resultado = print(f'Com {idade} anos: Voto Opcional')
    else:
        resultado = print(f'Com {idade} anos: Voto Obrigatório')


voto()
