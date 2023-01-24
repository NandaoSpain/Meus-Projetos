números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    usuário = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numeros[usuário]}')
    resp = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
    if resp not in 'Ss':
        break
