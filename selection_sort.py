#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 19:49:59 2022

@author: estanislau
"""

def selection_sort(vetor):
    tamanho_vetor = len(vetor)
    
    for i in range(tamanho_vetor):
        menor = i
        for j in range(i + 1, tamanho_vetor):
            if vetor[j] < vetor[menor]:
                menor = j
        vetor[menor], vetor[i] = vetor[i], vetor[menor]
        

vetor = [3, 15, 7, 12, 17, 1, 26, 4]
selection_sort(vetor)
print(vetor)