import os


tarefas = []
tarefas_refazer = []


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
    
    tarefas.append(tarefa)
    listar(tarefas)

while True:
    print('Comandos: listar, desfazer, refazer. ')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'adicionar': lambda: adicionar(tarefa, tarefas)
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()
    