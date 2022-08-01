#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 20:25:53 2022

@author: estanislau
"""

import numpy as np

def merge_sort(vetor):
    if len(vetor) > 1:
        divisao = len(vetor) // 2
        esquerda = vetor[:divisao].copy()
        direita = vetor[divisao:].copy()
        
        merge_sort(esquerda)
        merge_sort(direita)
        
        i = j = k = 0
        
        # ordena esquerda e direita
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1
        
        # ordenação final
        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1
        return vetor
    
    
vetor = np.array([15, 34, 8, 3, 98, 47])

vetor = merge_sort(vetor)
print(vetor)