analise = 0
ex = str(input('Digite uma expressão: '))
for simb in ex:
    if simb == '(':
        analise += 1
    if simb == ')':
        analise -= 1
if analise == 0:
    print('Sua expressão é válida')
else:
    print('Expressão INVÁLIDA')
