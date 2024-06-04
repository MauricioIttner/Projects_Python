# Formatando datas com datetime
# datetime.strptime('DATA', 'FORMATO')
# https://docs.python.org/pt-br/3/library/datetime.html
from datetime import datetime

fmt = '%d/%m/%Y'
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime(fmt))
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print('STR', data.strftime('%Y'), 'INT', data.year)
print('STR', data.strftime('%d'), 'INT', data.day)
print('STR', data.strftime('%m'), 'INT', data.month)
print('STR', data.strftime('%H'), 'INT', data.hour)
print('STR', data.strftime('%M'), 'INT', data.minute)
print('STR', data.strftime('%S'), 'INT', data.second)
