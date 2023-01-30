aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))
print('*' * 30)
print(f'  -Nome é igual a {aluno["Nome"]}')
print(f'  -Média é igual a {aluno["média"]}')
if aluno['média'] >= 7:
    print('  -Situação do aluno é APROVADO!')
else:
    print('  -Situação do aluno é REPROVADO!')
