#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 20:40:30 2022

@author: estanislau
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def show_node_data(self):
        print(self.data)
        
class Lista_Encadeada:
    
    def __init__(self):
        self.head = None
    
    def insere_inicio(self, valor):
        novo = Node(valor)
        novo.next = self.head
        self.head = novo
        # print(self.head)
    
    def excluir_inicio(self):
        if self.head is None:
            print("Lista vazia")
            return None
        temp = self.head
        self.head = self.head.next
        return temp
        
    def excluir_posicao(self, valor):
        if self.head is None:
            print("Lista vazia")
            return None
        
        atual = self.head
        anterior = self.head
        while atual.data != valor:
            if atual.next == None: 
                print("Não encontrou")
                return None
            else:
                anterior = atual
                atual = atual.next
        
        if atual == self.head:
            self.head = self.head.next
        else:
            anterior.next = atual.next
    
    def pesquisa(self, valor):
        if self.head is None:
            print("Lista vazia")
            return None
        temp = self.head
        
        while temp.data != valor:
            if temp.next == None: 
                print("Não encontrou")
                return None
            else:
                temp = temp.next
        return temp
    
    
    def mostrar(self):
        atual = self.head
        while atual is not None:
            atual.show_node_data()
            # print(atual)
            atual = atual.next
    
     
class Lista_Encadeada_Extrimidade_Dupla:
    
    def __init__(self):
        self.head = None
        self.last = None
       
    def __lista_vazia(self):
        return self.head == None
    
    def insere_inicio(self, valor):
        novo = Node(valor)
        if self.__lista_vazia():
            self.last = novo
        novo.next = self.head
        self.head = novo
        print(self.head)
        print(self.last)
    
    def insere_final(self, valor):
        novo = Node(valor)
        if self.__lista_vazia():
            self.head = novo
        else:
            self.last.next = novo
        self.last = novo
        print(self.head)
        print(self.last)
    
    
    def excluir_inicio(self):
        if self.__lista_vazia():
            print("Lista vazia")
            return None
        temp = self.head
        if self.head.next == None:
            self.last = None
        self.head = self.head.next
        return temp
        
    def excluir_posicao(self, valor):
        if self.head is None:
            print("Lista vazia")
            return None
        
        atual = self.head
        anterior = self.head
        while atual.data != valor:
            if atual.next == None: 
                print("Não encontrou")
                return None
            else:
                anterior = atual
                atual = atual.next
        
        if atual == self.head:
            self.head = self.head.next
        else:
            anterior.next = atual.next
    
    def pesquisa(self, valor):
        if self.head is None:
            print("Lista vazia")
            return None
        temp = self.head
        
        while temp.data != valor:
            if temp.next == None: 
                print("Não encontrou")
                return None
            else:
                temp = temp.next
        return temp
    
    
    def mostrar(self):
        if self.__lista_vazia():
            print("A lista está vazia")
            return 
        atual = self.head
        while atual is not None:
            atual.show_node_data()
            # print(atual)
            atual = atual.next
       
    
# lista = Lista_Encadeada()

# lista.insere_inicio(19)
# lista.insere_inicio(39)
# lista.insere_inicio(27)

# lista.mostrar()
# print()

# # lista.excluir_inicio()
# lista.excluir_posicao(39)
# # lista.excluir_inicio()
# # lista.excluir_inicio()

# lista.mostrar()
# print()

# print(lista.pesquisa(3))




lista = Lista_Encadeada_Extrimidade_Dupla()

lista.insere_inicio(19)
print()
lista.insere_final(39)
print()
lista.insere_final(27)

print()
lista.mostrar()

lista.excluir_inicio()

print()
lista.mostrar()

lista.excluir_inicio()

print()
lista.mostrar()
