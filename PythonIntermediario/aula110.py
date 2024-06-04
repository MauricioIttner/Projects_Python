# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

# Decorator
def create_func(func):
    def intern(*args, **kwargs):
        print('I will decorate you')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print('Okay, now you`ve been decorated')
        return result
    return intern


@create_func
def reverse_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param should be a string')


invertida = reverse_string('Mauricio')
print(invertida)
