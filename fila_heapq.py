#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:15:51 2022

@author: estanislau
"""
import heapq

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
   
    def __repr__(self):
        return self.nome
    
    
class Fila_De_Prioridade:
    
    def __init__(self):
        self.fila_de_prioridade = [] 
        self._indice = 0
        
    def inserir_na_fila(self, objeto, prioridade):
        heapq.heappush(self.fila_de_prioridade, (-prioridade, self._indice, objeto))
        self._indice += 1
        
    def retirar_da_fila(self):
        if len(self.fila_de_prioridade) > 0:
            heapq.heappop(self.fila_de_prioridade)[-1]
            
    def mostrar(self):
        print(self.fila_de_prioridade)
        
p1 = Pessoa("João")
p2 = Pessoa("Marcos")
p3 = Pessoa("Maria")
p4 = Pessoa("Carla")
p5 = Pessoa("Zezé")

fp = Fila_De_Prioridade()

fp.inserir_na_fila(p1, 20)
fp.inserir_na_fila(p2, 16)
fp.inserir_na_fila(p3, 25)
fp.inserir_na_fila(p4, 23)
fp.inserir_na_fila(p5, 20)

fp.mostrar()

fp.retirar_da_fila()
# fp.retirar_na_fila()

fp.mostrar()