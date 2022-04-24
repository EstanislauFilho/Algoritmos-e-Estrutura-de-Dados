#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 20:22:53 2022

@author: estanislau
"""

import time

class Fila:
    
    def __init__(self):
        self.fila = []
        self.contador = 0
        
    def inserir_na_fila(self, valor):
        """
        Insere valor sempre na ultima posição da lista
        """
        self.fila.append(valor)
        self.contador += 1
        
    def remover_na_fila(self):
        """
        Remove no inicio da fila somente se a mesma não estiver vazia
        """
        if self.contador > 0:
            self.fila.pop(0)
            self.contador -= 1
  
          
if __name__ == '__main__':
    t_ini = time.time()
    f = Fila()
    
    f.remover_na_fila()
    print(f.fila)
    
    f.inserir_na_fila(1)
    f.inserir_na_fila(2)
    f.inserir_na_fila(3)
    f.inserir_na_fila(4)
    f.inserir_na_fila(5)
    f.inserir_na_fila(6)
    
    f.remover_na_fila()
    print(f.fila)
    
    f.inserir_na_fila(6)
    f.inserir_na_fila(7)
    f.inserir_na_fila(8)
    f.inserir_na_fila(9)
    f.inserir_na_fila(9)
    
    f.remover_na_fila()
    f.remover_na_fila()
    f.remover_na_fila()
    
    
    print(f.fila)
    
    t_fim = time.time()
    print(f'Tempo de execução: {(t_fim - t_ini):.5f} seg')