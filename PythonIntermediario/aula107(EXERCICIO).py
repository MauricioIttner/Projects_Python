# copy, sorted, produtos.sort
# Exercícios
import copy
from dados import produtos

def imprimir(lista):
    for item in lista:
        print(item)
    print()
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)


novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]
print('Produtos ordenados com aumento de 10%: \n')
imprimir(novos_produtos)
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
	copy.deepcopy(produtos),
	key=lambda p: p['nome'], 
	reverse=True
)
print('Produtos ordenados em ordem decrescente: \n')
imprimir(produtos_ordenados_por_nome)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco = sorted(produtos, key=lambda item: item['preco'])
print('Produtos ordenados por preço crescente: \n')
imprimir(produtos_ordenados_por_preco)