#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 20:46:48 2022

@author: estanislau
"""

import time

class Matriz:
    
    def __init__(self):
        self.matriz = [[1, 2, 3], 
                       [4, 5, 6], 
                       [7, 8, 9],]
        
    def inserir_na_matriz(self, valor, pos_i, pos_j):
        """
        Insere valor nas posições i e j da matriz
        """
        self.matriz[pos_i][pos_j] = valor
        
    def remover_na_matriz(self, valor):
        """
        Remove o valor se o mesmo existir na matriz
        """
        for i, linha in enumerate(self.matriz):
            for j, coluna in enumerate(linha):
                if coluna == valor:
                    linha.remove(valor)
                    

  
          
if __name__ == '__main__':
    t_ini = time.time()
    m = Matriz()

    m.inserir_na_matriz(5, 2, 2)
    m.remover_na_matriz(15)
    
    print(m.matriz)
    
    t_fim = time.time()
    print(f'Tempo de execução: {(t_fim - t_ini):.5f} seg')