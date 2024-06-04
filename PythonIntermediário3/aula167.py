# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
# from pytz import timezone


# print(datetime.now(timezone('Europe/Dublin')))
data = datetime.now()
print(data.timestamp())
print(data.fromtimestamp(1709073759.908403))
# print(data)
# data_str = '2022-04-20 07:49:23'
# data_str = '20-04-2022 07:49:23'
# # data_str_fmt = '%Y-%m-%d %H:%M:%S'
# data_str_fmt = '%d-%m-%Y %H:%M:%S'

# # data = datetime(2022, 4, 20, 18, 57, 00)
# data = datetime.strptime(data_str, data_str_fmt)
