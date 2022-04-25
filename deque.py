#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Apr 24 20:48:16 2022

@author: estanislau
"""

import time

class Deque:
    
    def __init__(self):
        self.deque = []
        self.contador = 0
        
    def inserir_no_inicio_do_deque(self, valor):
        """
        Insere valor na primeira posição do deque
        """
        self.deque.insert(0, valor)
        self.contador += 1
        
    def inserir_no_final_do_deque(self, valor):
        """
        Insere valor na ultima posição do deque
        """
        self.deque.append(valor)
        self.contador += 1
        
    def remover_no_inicio_do_deque(self):
        """
        Remove no inicio do deque somente se a mesma não estiver vazia
        """
        if self.contador > 0:
            self.deque.pop(0)
            self.contador -= 1
            
    def remover_no_final_do_deque(self):
        """
        Remove no final do deque somente se a mesma não estiver vazia
        """
        if self.contador > 0:
            self.deque.pop(-1)
            self.contador -= 1
  
          
if __name__ == '__main__':
    t_ini = time.time()
    d = Deque()
    
    d.remover_no_inicio_do_deque()
    
    d.remover_no_final_do_deque()
    print(d.deque)
    
    d.inserir_no_inicio_do_deque(1)
    
    d.inserir_no_final_do_deque(2)
    d.inserir_no_final_do_deque(3)
    d.inserir_no_final_do_deque(4)
    
    d.inserir_no_inicio_do_deque(5)
    d.inserir_no_inicio_do_deque(6)
    
    d.remover_no_final_do_deque()
    print(d.deque)
    
    d.inserir_no_final_do_deque(6)
    d.inserir_no_final_do_deque(7)
    
    d.inserir_no_inicio_do_deque(8)
    d.inserir_no_inicio_do_deque(9)
    d.inserir_no_inicio_do_deque(9)
    
    d.remover_no_inicio_do_deque()
    
    d.remover_no_final_do_deque()
    print(d.deque)
    
    t_dim = time.time()
    print(f'Tempo de execução: {(t_dim - t_ini):.5f} seg')