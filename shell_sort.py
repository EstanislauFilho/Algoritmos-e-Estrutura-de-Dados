#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 20:02:13 2022

@author: estanislau
"""

import numpy as np

def shell_sort(vetor):
    intervalo = len(vetor) // 2
    
    while intervalo > 0:
        for i in range(intervalo, len(vetor)):
            temp = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            vetor[j] = temp
        intervalo //= 2
    return vetor
            

vetor = np.array([15, 34, 8, 3])

vetor = shell_sort(vetor)
print(vetor)