caminho_arquivo = 'C:\\Users\\Nandão\\Desktop\\Arquivo\\Exercício018.txt'

arquivo = open(caminho_arquivo, 'w+')

arquivo.close()


with open(caminho_arquivo, 'w+') as arquivo:
    ...