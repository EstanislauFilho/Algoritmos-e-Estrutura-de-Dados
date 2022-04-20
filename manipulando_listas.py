#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 13:23:34 2022

@author: estanislau
"""

lista = [1, 10, 16, 2, 9, 2, 3, 4, 5]

lista.insert(5, 13)
print(lista)

lista.remove(2)
print(lista)

lista.append(6)
print(lista)

lista.pop(7)
print(lista)

print(lista[-1])

print(lista[::-1])


lista = [i for i in range(10) if i % 2 == 0] # Compreensão de lista

print(lista)