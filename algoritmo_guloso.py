#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 11:51:16 2022

@author: estanislau
"""

moedas = [100, 50, 5, 1]
sol = []
soma = 0
troco = 66 # valor do troco

i = 0
while i < len(moedas) and soma != troco:
    if soma + moedas[i] <= troco:
        sol.append(moedas[i])
        soma += moedas[i]
    else:
         i += 1
        
print(sol)
