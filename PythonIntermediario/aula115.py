# count é um iterador sem fim
from itertools import count

c1 = count(step=3, start=3)
r1 = range(2, 50)

print('count')
for i in c1:
    if i > 50:
        break

    print(i)

print()
print('range')
for i in r1:
    if i > 50:
        break

    print(i)
