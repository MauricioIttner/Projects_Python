# Exercício - Lista de Tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café'] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import json
import os


# Cria listar, para listar tarefas
def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa a listar')
        print()
        return
    print('Tarefas:')
    print(*tarefas, sep='\n')
    print()


# Cria desfazer, para desfazer tarefas


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa a desfazer')
        return

    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    listar(tarefas)


# Cria refazer, para refazer tarefas


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa a refazer')
        return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    listar(tarefas)


# Cria adicionar, para adicionar na lista de tarefas


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nada.')
        return
    tarefas.append(tarefa)
    listar(tarefas)

# Le as tarefas


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe. Criando...')
        salvar(tarefas, caminho_arquivo)
    return dados

# Salva as tarefas em um arquivo json


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


# Criar lista de tarefas a cada tarefa digitada
CAMINHO_ARQUIVO = 'aula127.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []
# Mostrar comandos e perguntar qual deseja exercutar

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'adicionar': lambda: adicionar(tarefa, tarefas),
        'clear': lambda: os.system('cls')
    }
    comando = comandos.get(tarefa) if comandos.get(
        tarefa) is not None else comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)

# if tarefa == 'listar':
#     listar(tarefas)
#     continue
# elif tarefa == 'desfazer':
#     desfazer(tarefas, tarefas_refazer)
#     listar(tarefas)
#     continue
# elif tarefa == 'refazer':
#     refazer(tarefas, tarefas_refazer)
#     listar(tarefas)
#     continue
# elif tarefa == 'clear':
#     os.system('cls')
#     continue
# else:
#     adicionar(tarefa, tarefas)
#     listar(tarefas)
#     continue
