#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 20:26:52 2022

@author: estanislau
"""

class Pessoa:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade
        
    def obter_nome(self):
        return self.nome
    
    def obter_prioridade(self):
        return self.prioridade
    
    
class Fila_De_Prioridade:
    
    def __init__(self):
        self.fila_de_prioridade = [] 
        self.tamanho_fila = 0
        
    def inserir_na_fila(self, objeto):
        if self.tamanho_fila == 0:
            self.fila_de_prioridade.insert(0, objeto)
        else:
            inseriu_na_fila = False
            for i in range(self.tamanho_fila):
                if self.fila_de_prioridade[i].obter_prioridade() < objeto.obter_prioridade():
                    self.fila_de_prioridade.insert(i, objeto)
                    inseriu_na_fila = True
                    break
                
            if not inseriu_na_fila:
                self.fila_de_prioridade.insert(self.tamanho_fila, objeto)
        self.tamanho_fila += 1
        
    def remover_na_fila(self):
        if self.tamanho_fila != 0:
            self.fila_de_prioridade.pop(0)
            self.tamanho_fila -= 1
            
    def mostrar(self):
        for elem in self.fila_de_prioridade:
            print(f"Nome: {elem.obter_nome()}", end= " ")
            print(f"\t\tPior: {elem.obter_prioridade()}")
        print()
        
p1 = Pessoa("João", 8)
p2 = Pessoa("Marcos", 36)
p3 = Pessoa("Maria", 14)
p4 = Pessoa("Carla", 40)

fp = Fila_De_Prioridade()

fp.inserir_na_fila(p1)
fp.inserir_na_fila(p2)
fp.inserir_na_fila(p3)
fp.inserir_na_fila(p4)

fp.mostrar()

fp.remover_na_fila()
fp.remover_na_fila()

fp.mostrar()