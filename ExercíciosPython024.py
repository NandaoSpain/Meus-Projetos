from datetime import date
funcionario = {}
funcionario['nome'] = str(input('Nome: '))
nasc = (int(input('Ano de Nascimento: ')))
funcionario['idade'] = date.today().year - nasc
funcionario['ctps'] = int(input('Carteira de Trabalho [0 não tem]: '))
if funcionario['ctps'] != 0:
    anoctt = int(input('Ano de Contratação: '))
    funcionario['ano de contratação'] = anoctt
    funcionario['salario'] = int(input('Salário R$:'))
    funcionario['aposentadoria'] = (anoctt + 35) - nasc
print('-=' * 25)
for k, v in funcionario.items():
    print(f'{k} tem o valor {v}')
