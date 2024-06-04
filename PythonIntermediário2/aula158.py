# Funções decoradoras e decoradores com classes
def adiciona_repr(class_):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    class_.__repr__ = meu_repr
    return class_


# class MyReprMixing:
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


# Time = adiciona_repr(Time)
brasil = Time('Brasilia')
portugal = Time('Portugal')
# Planeta = adiciona_repr(Planeta)
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(marte)
