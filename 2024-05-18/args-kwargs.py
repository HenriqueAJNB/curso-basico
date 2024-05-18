def soma(*args, **kwargs):
    # a=10, b=50, args=(), kwards={...}
    return sum(args) + sum(kwargs.values())


resultado = soma(10, 50, 60, 30, 40, 1, c=3, d=4, e=6, f=20)
print(resultado)
