# Ordem dos Decoradores

def decorator_parameters(name):
    def decorator(func):
        print('Decorator:', name)

        def new_function(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {name=}'
            return final
        return new_function
    return decorator


@decorator_parameters(name='first')
def sum_(x, y):
    return x+y


ten_plus_five = sum_(10, 5)
print(ten_plus_five)
