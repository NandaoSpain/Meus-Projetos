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