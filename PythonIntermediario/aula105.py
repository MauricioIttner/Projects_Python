import importlib as lib
import aula105_m as aa

print(aa.variavel)

for i in range(10):
    lib.reload(aa)
    print(i)
