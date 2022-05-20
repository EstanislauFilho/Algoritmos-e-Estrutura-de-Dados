#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 16:17:04 2022

@author: estanislau
"""

import sys

class Tabela_Hash:
    
    def __init__(self, tamanho_tabela):
        
        if tamanho_tabela < 1:
            print('Erro: o tamanho da tabela tem que ser positivo')
            sys.exit(1)
        
        self.tamanho_tabela = tamanho_tabela
        self.tabela = [[] for i in range(self.tamanho_tabela)]
        
    def funcao_hash(self, chave):
        return chave % self.tamanho_tabela
    
    def inserir_na_tabela_hash(self, chave):
        self.tabela[self.funcao_hash(chave)].append(chave)
    
    def buscar_na_tabela_hash(self, chave):
        if chave in self.tabela[self.funcao_hash(chave)]:
            return True
        return False
    
    def mostrar(self):
        for lista in self.tabela:
            if lista: # se lista nao estiver vazia
                for chave in lista:
                    print(chave, end=" ")
                print()
        
th = Tabela_Hash(9)

th.inserir_na_tabela_hash(19)
th.inserir_na_tabela_hash(28)
th.inserir_na_tabela_hash(20)
th.inserir_na_tabela_hash(5)
th.inserir_na_tabela_hash(33)
th.inserir_na_tabela_hash(15)

th.inserir_na_tabela_hash(17)
th.inserir_na_tabela_hash(2)
th.inserir_na_tabela_hash(4)
th.inserir_na_tabela_hash(50)
th.inserir_na_tabela_hash(23)
th.inserir_na_tabela_hash(189)

th.mostrar()