#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:55:39 2022

@author: estanislau
"""
import numpy as np

class Fila_Circular:
    
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.fila = np.empty(self.capacidade, dtype=int)
        
    def __fila_vazia(self):
        # verifica se a fila está vazia
        return self.numero_elementos == 0
    
    def __fila_cheia(self):
        # verifica se a fila está cheia
        return self.numero_elementos == self.capacidade
    
    def inserir(self, valor):
        if self.__fila_cheia():
            print("fila cheia")
            return 
        
        if self.final == self.capacidade - 1:
            # se chegou no final da fila, começa a preencher nos espaços vazios
            self.final = -1
        self.final += 1
        self.fila[self.final] = valor # insere no final da fila
        self.numero_elementos += 1
        
    def remover(self):
        if self.__fila_vazia():
            print("fila vazia")
            return
        
        temp = self.fila[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade:
            # se chegou no final da fila, retorna para o inicio
            self.inicio = 0
        self.numero_elementos -= 1
        return temp  
    
    def primeiro(self):
        if self.__fila_vazia():
            return -1
        # retorna o elemento da primeira posição
        return self.fila[self.inicio]
            
fila = Fila_Circular(5)

print(fila.primeiro())

fila.inserir(3)
fila.inserir(17)
fila.inserir(6)
fila.inserir(78)
fila.inserir(32)

fila.remover()


print(fila.primeiro())