#!/usr/bin/python3.10

from operator import itemgetter
import sys

def nouveau_point(
    x: float, y: float = 0, /,
    z: float = 0, *args, #
    color: str = 'red', temperature: float = 25, **kwargs
) -> dict:

    if len(args) > 0:
        print(f"Paramètres non nommés ignorés : {args}")
    
    if len(kwargs) > 0:
        print(f"Paramètres nommés ignorés: {kwargs}")

    return {
        'x': x, 'y': y, 'z': z, 'color': color, 'temperature': temperature, 
    }

# print(nouveau_point(1, 2, color = 'blue'))

def f(a, b, /):
    print(a, b)

# f(b = 5, a = 6) # Génère une erreur
f(5, 6) # Donne 5 6

def g(*, a, b):
    print(a, b)

# g(5, 6) # Génère une erreur
g(b = 5, a = 6) # Donne 6 5

f = lambda x: x[1]

x = [('Laurent', 20), ('gilles', 40)]

print(sorted(x, key=lambda x: x[1]))

print(sys.version)