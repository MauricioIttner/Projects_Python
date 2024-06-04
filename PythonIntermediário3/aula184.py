# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula184-ex.csv'

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=';')
    for linha in leitor:
        print(linha['Nome'])
# with CAMINHO_CSV.open('r') as arquivo:
#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)
