import json
caminho_arquivo = 'C:\\Users\\Nandão\\Desktop\\Arquivo\\Exercício018.txt'

arquivo = open(caminho_arquivo, 'w+')

arquivo.close()


with open(caminho_arquivo, 'w+') as arquivo:
    ...


pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula117.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)
