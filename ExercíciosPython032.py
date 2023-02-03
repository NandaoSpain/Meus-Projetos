def voto():
    print('-' * 30)
    from datetime import date
    nasc = int(input('Em que ano você nasceu? '))
    idade = date.today().year - nasc
    resultado = ''
    if idade < 16:
        resultado = 'Não Vota'
    elif 16 <= idade < 18 or idade > 65:
        resultado = 'Voto Opcional'
    else:
        resultado = 'Voto Obrigatório'
        

    print(f'Com {idade} anos: {resultado}')


voto()
