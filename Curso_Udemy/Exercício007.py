print('Validador de CPF'.center(40))
cpf = '060.851.029-76'
cpf_puro = []
multiplicador = [10, 9, 8, 7, 6, 5, 4, 3, 2]
for c in cpf:
    if c != '.' and c != '-':
        inteiro = int(c)
        cpf_puro.append(inteiro)
cpf_manipular = cpf_puro[:]
cpf_puro.pop(-1)
cpf_puro.pop(-1)
pos = 0
resultado1 = 0
for c in cpf_puro:
    resultado1 += c * multiplicador[pos]
    pos += 1
resultado2 = resultado1 * 10
resultado3 = resultado2 % 11
cpf_puro.append(resultado3)
print(cpf_puro)

