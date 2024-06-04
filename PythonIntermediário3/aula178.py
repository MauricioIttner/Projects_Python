# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'OneDrive\\Área de Trabalho')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO_AULA178')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')

# os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     # Cria todas as pastas conforme a pasta original
#     # Para assim permitir a copia de arquivos
#     for dir_ in dirs:
#         caminho_novo_diretorio = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)
#         os.makedirs(caminho_novo_diretorio, exist_ok=True)

# # Pega os arquivos de dentro da pasta e copia para outra pasta
#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         caminho_novo_arquivo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
#         shutil.copy(caminho_arquivo, caminho_novo_arquivo)
