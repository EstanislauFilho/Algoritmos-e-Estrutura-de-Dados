#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 21:33:00 2022

@author: estanislau
"""

# Gerando subconjuntos utilizando backtracking
def gerar_subconjuntos(S, vet, K, N):
    if K == N:
        print("{", end=" ")
        for i in range(N):
            if vet[i] == True:
                print(S[i], end=" ")
        print("}")
    else:
        vet[K] = True
        gerar_subconjuntos(S, vet, K + 1, N)
        vet[K] = False
        gerar_subconjuntos(S, vet, K + 1, N)
        
S = [1, 2]
tamS = len(S)
vet = [False for i in range(tamS)]

gerar_subconjuntos(S, vet, 0, tamS)