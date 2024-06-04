# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import locale
import string
from datetime import datetime
from pathlib import Path
# import json

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula188.txt'


# Usa o local padrão do computador
locale.setlocale(locale.LC_ALL, '')


def convert_to_brl(number: float | int) -> str:
    # Symbol=False -> Não Mostra o simbolo de dinheiro
    # Grouping=True -> agrupa os numeros com sua respectiva casas
    brl = 'R$ ' + locale.currency(val=number, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 20)
dados = dict(
    nome='João',
    valor=convert_to_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (22) 4002-8922'

)

# print(json.dumps(dados, indent=2, ensure_ascii=False))


class MyTemplate(string.Template):
    delimiter = '%'


with CAMINHO_ARQUIVO.open('r', encoding='utf8') as file:
    text = file.read()
    template = string.Template(text)
    print(template.substitute(dados))

# texto = '''
#  Prezado(a) %nome,

#  Informamos que sua mensalidade será cobrada no valor de %{valor}
    # no dia %data.
#  Caso deseje cancelar o serviço, entre em contato com a %empresa pelo
# telefone %telefone.

#  Atenciosamente,

#  %{empresa}
#  '''
# template = MyTemplate(texto)
# print(template.substitute(dados))
