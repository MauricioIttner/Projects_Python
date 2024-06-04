import sys

# Generator expression, Iterables, Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__e__next__
lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))


for n in generator:
    print(n)
# print(next(iterator))

# for palavra in iterator:
#     print(palavra)
