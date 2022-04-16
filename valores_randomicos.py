#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 17:47:30 2022

@author: estanislau
"""

import random

print(random.randrange(4)) # imprime valores entre 0 e 3

print(random.randint(1, 4)) # imprime valores entre 1 e 4

lista = [1, 3, 5, 9]

print(random.choice(lista)) # escolher um valor aleatório da lista

random.shuffle(lista) # embaralha os valores da lista

print(lista) 

print(random.sample(lista, 3)) # obtem três valores da lista em ordem aleatoria

print(random.random()) # gera valores aleatórios, também em ponto flutuante

print(random.uniform(1, 10)) # gera valores aleatórios fluatuante entre 1 e 9 