import os
import json

def listar(tarefas):
    print()
    os.system('cls')
    if not tarefas:
        print('Nada para listar')
        print()
        return
    
    print('TAREFAS'.center(20))
    for x in tarefas:
        print(f'\t{x}')
    print()
    

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nada para desfazer')
        print()
        return
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nada para refazer')
        print()
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    if tarefa is None:
        print('Você não adicionou nenhuma tarefa')
    
    
    lista_de_tarefas.append(tarefa)
    listar(tarefas)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
            dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


caminho_arquivo = 'listadetarefas.json'

tarefas = ler([], caminho_arquivo)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer. ')
    tarefa = input('Digite uma tarefa ou comando: ')
    if tarefa == 'sair':
        break
    comandos = {
        'listar': lambda: listar(tarefas),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()
    salvar(tarefas, caminho_arquivo)
    
