#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 21:04:33 2022

@author: estanislau
"""

class Nó:
    
    def __init__(self, chave):
        self.chave = chave
        self.filho_esquerda = None
        self.filho_direita = None
        
    def obter_chave(self):
        return self.chave
    
    def inserir_chave(self, chave):
        self.chave = chave
    
    def obter_filho_esquerda(self):
        return self.filho_esquerda
    
    def inserir_filho_esquerda(self, esquerda):
        self.filho_esquerda = esquerda
        
    def obter_filho_direita(self):
        return self.filho_direita
    
    def inserir_filho_direita(self, direita):
        self.filho_direita = direita
        

class Arvore_Binaria_Busca:
    
    def __init__(self):
        self.raiz = None
        
    def inserir_na_arvore(self, chave):
        nó = Nó(chave) # Cria um novo nó
        
        if self.raiz is None:
            self.raiz = nó
        
        else:
            # árvore não vazia, insere recursivamente
            
            nó_pai = None
            nó_atual = self.raiz
            
            while True:
                
                if nó_atual != None:
                    
                    nó_pai = nó_atual
        
                    # verifica se vai para esquerda ou direita
                    if nó.obter_chave() < nó_atual.obter_chave():
                        nó_atual = nó_atual.obter_filho_esquerda()  # vai para esquerda
                    else:
                        nó_atual = nó_atual.obter_filho_direita()   # vai para direta
                else:
                    
                    # Se atual é None, então encontrou onde inserir
                    if nó.obter_chave() < nó_pai.obter_chave():
                        nó_pai.inserir_filho_esquerda(nó)  # vai para esquerda
                    else:
                        nó_pai.inserir_filho_direita(nó)   # vai para direta
                        
                    break
                
    def mostrar(self, nó_atual):
        
        if nó_atual != None:
            print(nó_atual.obter_chave(), end=' ')
            self.mostrar(nó_atual.obter_filho_esquerda())
            self.mostrar(nó_atual.obter_filho_direita())
       
    def obter_raiz(self):
        return self.raiz
    
abb = Arvore_Binaria_Busca()

abb.inserir_na_arvore(8)
abb.inserir_na_arvore(3)
abb.inserir_na_arvore(1)
abb.inserir_na_arvore(6)
abb.inserir_na_arvore(4)
abb.inserir_na_arvore(7)
abb.inserir_na_arvore(10)
abb.inserir_na_arvore(14)
abb.inserir_na_arvore(13)

abb.mostrar(abb.obter_raiz())