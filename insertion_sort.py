#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 20:18:02 2022

@author: estanislau
"""

def insertion_sort(vetor):
    tamanho_vetor = len(vetor)
    
    for i in range(1, tamanho_vetor):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave

vetor = [3, 15, 7, 12, 17, 1, 26, 4]
insertion_sort(vetor)
print(vetor)