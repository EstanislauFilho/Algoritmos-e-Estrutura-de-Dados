#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:43:28 2022

@author: estanislau
"""

lista = [1, 2, 3, 4, 5]

f = filter(lambda x: x % 2 == 0, lista)

print(lista)
for i in f:
    print(i)