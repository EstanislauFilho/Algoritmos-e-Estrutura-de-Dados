#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 20:06:30 2022

@author: estanislau
"""
import time
class Pilha:
    
    def __init__(self):
        self.pilha = []
        self.contador = 0
        
    def inserir_na_pilha(self, valor):
        """
        Insere valor sempre na ultima posição da lista
        """
        self.pilha.append(valor)
        self.contador += 1
        
    def remover_na_pilha(self):
        """
        Remove no topo da pilha somente se a mesma não estiver vazia
        """
        if self.contador > 0:
            self.pilha.pop(-1)
            self.contador -= 1
  
          
if __name__ == '__main__':
    t_ini = time.time()
    p = Pilha()
    
    p.remover_na_pilha()
    
    p.inserir_na_pilha(1)
    p.inserir_na_pilha(2)
    p.inserir_na_pilha(3)
    p.inserir_na_pilha(4)
    p.inserir_na_pilha(5)
    p.inserir_na_pilha(6)
    
    p.remover_na_pilha()
    
    p.inserir_na_pilha(6)
    p.inserir_na_pilha(7)
    p.inserir_na_pilha(8)
    p.inserir_na_pilha(9)
    p.inserir_na_pilha(9)
    
    p.remover_na_pilha()
    
    print(p.pilha)
    
    t_fim = time.time()
    print(f'Tempo de execução: {(t_fim - t_ini):.5f} seg')