# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o emprestimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

emprestimo = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos
fmt = '%d/%m/%Y'
# print('Data inicial: ', datetime.strftime(data_emprestimo, fmt))
# print('Data final: ', datetime.strftime(data_final, fmt))
data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = emprestimo / numero_parcelas


print('Numero de parcelas:', numero_parcelas)

for data in data_parcelas:
    print(data.strftime(fmt), f'R$ {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R${emprestimo:,.2f} para pagar'
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R${valor_parcela:,.2f}'
)
