#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:11:35 2022

@author: estanislau
"""

class Nó:
    
    def __init__(self, label):
        self.label = label
        self.proximo = None
        
    def obter_label(self):
        return self.label
    
    def inserir_label(self, label):
        self.label = label
    
    def obter_proximo(self):
        return self.proximo
    
    def inserir_proximo(self, proximo):
        self.proximo = proximo
        
        
class Lista_Ligada:
    
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho_lista = 0
        
    def inserir_lista(self, label, index):
        
        if index >= 0:
            nó = Nó(label) #Cria o novo nó
            
            # verifica se a lista está vazia
            if self.empty():
                self.primeiro = nó
                self.ultimo = nó
            else:
                if (index == 0):
                    # inserão no início da lista
                    nó.inserir_proximo(self.primeiro)
                    self.primeiro = nó
                elif (index >= self.tamanho_lista):
                    # inserão no final da lista
                    self.ultimo.inserir_proximo(nó)
                    self.ultimo = nó
                else:
                    # inserão no meio da lista
                    nó_anterior = self.primeiro
                    nó_atual = self.primeiro.obter_proximo()
                    indice_atual = 1
                    
                    while nó_atual != None:
                        if indice_atual == index:
                            nó.inserir_proximo(nó_atual) # seta o nó atual para o próximo nó
                            nó_anterior.inserir_proximo(nó) # seta o nó como próximo do nó anterior
                            break
                        
                        nó_anterior = nó_atual
                        nó_atual = nó_atual.obter_proximo()
                        indice_atual += 1
                        
            self.tamanho_lista += 1 # atualiza o tamanho da lista    
                    
            
    def remocao_lista(self, index):
        if not self.empty() and index >= 0 and index < self.tamanho_lista:
            flag_remocao = False
            
            if self.primeiro.obter_proximo() == None:
                # quando possui apenas um elemento
                self.primeiro = None
                self.ultimo = None
                flag_remocao = True
                
            elif index == 0:
                # remove do inicio, mas possui mais de 1 elemento
                self.primeiro.obter_proximo()
                flag_remocao = True
                
            else:
                # Se chegou aqui é porque a lista possui mais de 1 elemento e a remoção não é no início
                nó_anterior = self.primeiro
                nó_atual = self.primeiro.obter_proximo()
                indice_atual = 1
                
                while nó_atual != None:
                    
                    if indice_atual == index:
                        nó_anterior.inserir_proximo(nó_atual.obter_proximo()) # o proximo do anterior aponta para o proximo do nó corrente
                        nó_atual.inserir_proximo(None) # seta o nó como próximo do nó anterior
                        flag_remocao = True
                        break
                    
                    nó_anterior = nó_atual
                    nó_atual = nó_atual.obter_proximo()
                    indice_atual += 1
                
            if flag_remocao:
                self.tamanho_lista -= 1 # atualiza o tamanho da lista    
                
    def empty(self):
        if self.primeiro == None:
            return True
        return False
    
    
    def mostrar(self):
        nó_atual = self.primeiro
        
        while(nó_atual != None):
            print(nó_atual.obter_label(), end=' ')
            nó_atual = nó_atual.obter_proximo()
        print()
        
        
# Teste
lista = Lista_Ligada()

lista.inserir_lista('Marcos', 0)

lista.mostrar()

lista.inserir_lista('Maria', 0)
lista.inserir_lista('Pedro', 1)

lista.mostrar()

lista.inserir_lista('Carlos', 0)
lista.mostrar()

lista.inserir_lista('Katarina', 2)
lista.mostrar()

lista.inserir_lista('Sara', 6)
lista.mostrar()

lista.remocao_lista(2)
lista.mostrar()


lista.remocao_lista(4)
lista.mostrar()