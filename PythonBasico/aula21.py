# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy
# 0 0.0  ''(String vazia) sao considerados False
# Também existe o tipo none que é usado
# para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha = int(input('Digite a senha: '))
senha_correta = 12345
if entrada == 'E' and senha == senha_correta:
    print('Entrou')
elif entrada == 'S':
    print('Saiu')
else:
    print('Valor incorreto')
    
#Valor de curto circuito
print(True and True and True)