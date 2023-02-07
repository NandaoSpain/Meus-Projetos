def leiaInt(msg):
    global valor
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO! Por favor digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor


def leiaFloat(msg):
    while True:
        try:
            r = float(input(msg))
        except(TypeError, ValueError):
            print(f'\033[0;31mERRO! Por favor digite um número real válido!\033[m')
            continue
        else:
            return r


inteiro = leiaInt('Digite um número: ')
real = leiaFloat('Digite um valor REAL: ')
print(f'O valor inteiro digitado foi {valor} e o valor real foi {real}')