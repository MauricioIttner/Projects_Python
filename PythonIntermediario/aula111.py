# Decoradores com parâmetros
def factory_decorators(a=None, b=None, c=None):
    def function_factory(func):
        print('Decorator 1')

        def nested(*args, **kwargs):
            print('Nested')
            res = func(*args, **kwargs)
            return res
        return nested
    return factory_decorators


@factory_decorators(1, 2, 3)
def soma(x, y):
    return x + y


multiplica = factory_decorators()(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
