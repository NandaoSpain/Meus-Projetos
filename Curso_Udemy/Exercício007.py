print('Validador de CPF'.center(40))
cpf = input('Digite um CPF para comprovação: ')
cpf_puro = []   
multiplicador1 = 10
for c in cpf:
    if c != '.' and c != '-':
        inteiro = int(c)
        cpf_puro.append(inteiro)
cpf_manipular = cpf_puro[:]
cpf_puro.pop(-1)
cpf_puro.pop(-1)
resultadosoma1 = 0
for c in cpf_puro:
    resultadosoma1 += c * multiplicador1
    multiplicador1 -= 1 
resultado = resultadosoma1 * 10 % 11
primeiro_digito = resultado if resultado <= 9 else 0
cpf_puro.append(primeiro_digito)

resultadosoma2 = 0
multiplicador2 = 11
for c in cpf_puro:
    resultadosoma2 += c * multiplicador2
    multiplicador2 -= 1
resultado2 = resultadosoma2 * 10 % 11
segundo_digito = resultado2 if resultado2 <=9 else 0
cpf_puro.append(segundo_digito)
if cpf_puro == cpf_manipular:
    print('CPF Válido!')
else:
    print('CPF INVÁLIDO!')
