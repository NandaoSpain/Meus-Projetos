def notas(*n, sit=False):
    """
    --> Função que retorna um dicionácio com as notas de um aluno, exibe maior nota,
    menor nota, média de notas, e situação atual
    :param n: uma ou mais notas 
    :param sit: valor opcional, informa a situação da turma
    :return: dicionário com várias informações da turma
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 3.5, sit=True)
print(resp)
