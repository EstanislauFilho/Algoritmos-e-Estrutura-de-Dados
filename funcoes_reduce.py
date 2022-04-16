#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:24:01 2022

@author: estanislau
"""

import functools

lista = [1, 2, 3, 4, 5]

r = functools.reduce(lambda x, y: x + y, lista)

print(lista)
print(r)