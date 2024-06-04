"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/3/tutorial/floatingpoint.html
"""

numero_1 = 0.10
numero_2 = 0.70
numero_3 = numero_1 + numero_2

print(round(numero_3, 3))
