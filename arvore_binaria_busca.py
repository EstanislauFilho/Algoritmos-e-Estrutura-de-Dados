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
         
                
    def remover_na_arvore(self, chave):
        nó_pai = None
        nó_atual = self.raiz
        
        while nó_atual != None:
            if chave == nó_atual.obter_chave():
                
                # nó a ser removido não possui filhos (nó folha)
                if nó_atual.obter_filho_esquerda() == None and nó_atual.obter_filho_direita() == None:
                    
                    # verifica se é a raiz
                    if nó_pai == None:
                        self.raiz = None
                    else:
                        # verifica se é fiho a direita ou a esquerda
                        if nó_pai.obter_filho_esquerda() == nó_atual:
                            nó_pai.inserir_filho_esquerda(None)
                        elif nó_pai.obter_filho_direita() == nó_atual:
                            nó_pai.inserir_filho_direita(None)
                            
                # nó a ser removido possui somente um filho 
                elif (nó_atual.obter_filho_esquerda() == None and nó_atual.obter_filho_direita() != None) or \
                        (nó_atual.obter_filho_esquerda() != None and nó_atual.obter_filho_direita() == None):
                     # verifica se é a raiz
                    if nó_pai == None:
                        if nó_atual.obter_filho_esquerda() != None:
                            self.raiz = nó_atual.obter_filho_esquerda()
                        else:
                            self.raiz = nó_atual.obter_filho_direita()
                    else:
                        # verifica se o filho do nó_atual é o fiho da esquerda
                        if nó_atual.obter_filho_esquerda() != None:
                            if nó_pai.obter_filho_esquerda() and nó_pai.obter_filho_esquerda().obter_chave() == nó_atual.obter_chave():
                                nó_pai.inserir_filho_esquerda(nó_atual.obter_filho_esquerda())
                            else:
                                nó_pai.inserir_filho_direita(nó_atual.obter_filho_esquerda())
                            
                        else: # senão o filho do nó_atual é o fiho da direita
                            # verifica se nó atual é filho à esquerda    
                            if nó_pai.obter_filho_esquerda() and nó_pai.obter_filho_esquerda().obter_chave() == nó_atual.obter_chave():
                                nó_pai.inserir_filho_esquerda(nó_atual.obter_filho_direita())
                            else:
                                nó_pai.inserir_filho_direita(nó_atual.obter_filho_direita())
                            
                # nó a ser removido  possui dois filhos
                elif (nó_atual.obter_filho_esquerda() != None and nó_atual.obter_filho_direita() != None):
                   
                    nó_pai_menor = nó_atual
                    nó_menor = nó_atual.obter_filho_direita()
                    proximo_menor = nó_atual.obter_filho_direita().obter_filho_esquerda()
                    
                    while proximo_menor != None:
                        nó_pai_menor = nó_menor
                        nó_menor = proximo_menor
                        proximo_menor = nó_menor.obter_filho_esquerda
                    
                    # verifica se o nó a ser removido é a raiz
                    if nó_pai == None:
                        
                        # Caso especial: o nó que ser a nova raiz é o filho da raiz
                        if self.raiz.obter_filho_direita().obter_chave() == nó_menor.obter_chave():
                            nó_menor.inserir_filho_esquerda(self.raiz.obter_filho_esquerda())
                        else:
                            # Verifica se o nó_menor é filho à esquerda ou à direita para setar para None o nó_menor
                            if nó_pai_menor.obter_filho_esquerda() and nó_pai_menor.obter_filho_esquerda().obter_chave() == nó_menor.obter_chave():
                                nó_pai_menor.inserir_filho_esquerda(None)
                            else:
                                nó_pai_menor.inserir_filho_direita(None)
                                
                            # seta os filhos á direita e esquerda de nó_menor
                            nó_menor.inserir_filho_esquerda(nó_atual.obter_filho_esquerda())
                            nó_menor.inserir_filho_direita(nó_atual.obter_filho_direita())
                                
                        # faz com que o nó_menor seja a raiz
                        self.raiz = nó_menor
                       
                    else:
                        # verifica se nó_atual é filho à esquerda ou à direita para setar o nó_menor como filho
                        # do pai do nó_atual
                        if nó_pai.obter_filho_esquerda() and nó_pai.obter_filho_esquerda().obter_chave() == nó_atual.obter_chave():
                            nó_pai.inserir_filho_esquerda(nó_menor)
                        else:
                            nó_pai.inserir_filho_direita(nó_menor)
                            
                        # verifica se o nó_menor é filho à esquerda ou à direita para setar para None o nó_menor
                        if nó_pai_menor.obter_filho_esquerda() and nó_pai_menor.obter_filho_esquerda().obter_chave() == nó_menor.obter_chave():
                            nó_pai_menor.inserir_filho_esquerda(None)
                        else:
                            nó_pai_menor.inserir_filho_direita(None)
                        
                        # seta os filhos á direita e esquerda de nó_menor
                        nó_menor.inserir_filho_esquerda(nó_atual.obter_filho_esquerda())
                        nó_menor.inserir_filho_direita(nó_atual.obter_filho_direita())
                        
                break
             
            nó_pai = nó_atual

            # verifica se vai para esquerda ou direita
            if chave < nó_atual.obter_chave():
                # vai para esquerda
                nó_atual = nó_atual.obter_filho_esquerda()
            else:
                # vai para direita
                nó_atual = nó_atual.obter_filho_direita()
            
                        
    def mostrar(self, nó_atual):
        
        if nó_atual != None:
            print(nó_atual.obter_chave(), end=' ')
            self.mostrar(nó_atual.obter_filho_esquerda())
            self.mostrar(nó_atual.obter_filho_direita())
       
    def obter_raiz(self):
        return self.raiz


# abb = Arvore_Binaria_Busca()

# abb.inserir_na_arvore(8)
# abb.inserir_na_arvore(3)
# abb.inserir_na_arvore(1)
# abb.inserir_na_arvore(6)
# abb.inserir_na_arvore(4)
# abb.inserir_na_arvore(7)
# abb.inserir_na_arvore(10)
# abb.inserir_na_arvore(14)
# abb.inserir_na_arvore(13)

# abb.remover_na_arvore(8)

# abb.mostrar(abb.obter_raiz())
# print()



# Segunda Versão

class Node:
    def __init__(self, data):
        self.data = data
        self.esquerda = None
        self.direita = None
        
    def show_node_data(self):
        print(self.data)



class Arvore_Binaria_Busca_2:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo = Node(valor)
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                if valor < atual.data:
                    atual = atual.esquerda
                    if atual == None:
                        pai.esquerda = novo
                        return
                else:
                    atual = atual.direita
                    if atual == None:
                        pai.direita = novo
                        return








abb = Arvore_Binaria_Busca_2()

abb.inserir(53)
abb.inserir(30)
abb.inserir(14)
abb.inserir(39)
abb.inserir(9)
abb.inserir(23)
abb.inserir(34)
abb.inserir(49)
abb.inserir(72)
abb.inserir(61)
abb.inserir(84)
abb.inserir(79)

print(abb.raiz.direita.data)














    




