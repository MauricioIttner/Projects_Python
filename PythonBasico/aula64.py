"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
# condicao = 10 == 11
# vrv = ('Valor') if condicao else ('Outro valor')
# print(vrv)

digito = 1
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
