#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:40:23 2022

@author: estanislau
"""


#####################################################
# Demonstração função filter
lista_filter = [1, 2, 3, 4, 5]

f = filter(lambda x: x % 2 == 0, lista_filter)

print(lista_filter)
for i in f:
    print(i)
#####################################################   
    

#####################################################
# Demonstração função lambda
def fatorial(n):
    if n == 0:
        return 1
    return (n * fatorial(n-1))

fatorial_lambda = lambda n: n * fatorial(n-1) if n > 1 else 1

print(fatorial_lambda(3))
#####################################################


#####################################################
# Demonstração função map
lista_map = [1, 2, 3]

m = map(lambda x: x ** 2, lista_map)

for i in m:
    print(i)
#####################################################


#####################################################
# Demonstração função reduce
import functools

lista = [1, 2, 3, 4, 5]

r = functools.reduce(lambda x, y: x + y, lista)

print(lista)
print(r)
#####################################################