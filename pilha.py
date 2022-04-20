#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 20:06:30 2022

@author: estanislau
"""

class Pilha:
    
    def __init__(self):
        self.pilha = []
        
    def inserir_na_pilha(self, valor):
        """
        Insere valor sempre na ultima posição da lista
        """
        self.pilha.append(valor)
        
    def remover_na_pilha(self):
        """
        Remove no topo da pilha somente se a mesma não estiver vazia
        """
        if len(self.pilha) > 0:
            self.pilha.pop(len(self.pilha)-1)

  
          
if __name__ == '__main__':
    p = Pilha()
    
    p.remover_na_pilha()
    
    p.inserir_na_pilha(5)
    p.inserir_na_pilha(9)
    p.inserir_na_pilha(34)
    
    p.remover_na_pilha()
    
    print(p.pilha)