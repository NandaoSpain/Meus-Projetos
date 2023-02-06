def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if not formato else din(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if not formato else din(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else din(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else din(res)


def din(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, aum=0, red=0):
    dic = {'Preço Analisado:', preço,
           'Dobro do Preço:', dobro(preço),
           'Metade do Preço:', metade(preço),
           f'{aum} de Aumento:', aumentar(preço),
           f'{red} de Redução:', diminuir(preço)}
    print('-' * 30)
    print(f'{"Resumo do Valor":^30}')
    print('-' * 30)
    print(f'Preço Analisado:   \t{din(preço):>}')
    print(f'Dobro do Preço:    \t{dobro(preço, True):>}')
    print(f'Metade do Preço:   \t{metade(preço, True):>}')
    print(f'Aumento de {aum}%: \t{aumentar(preço, aum, True):>}')
    print(f'Redução de {red}%: \t{diminuir(preço, red, True):>}')
    print('-' * 30)
