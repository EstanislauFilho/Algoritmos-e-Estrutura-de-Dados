#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 10:19:12 2022

@author: estanislau
"""
from collections import defaultdict

class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def obter_nome(self):
        return self.nome
    
    def obter_idade(self):
        return self.idade
    
    
class Amizade:
    
    def __init__(self, pessoa_1, pessoa_2):
        self.pessoa_1 = pessoa_1 
        self.pessoa_2 = pessoa_2
        
    def obter_pessoa_1(self):
        return self.pessoa_1
    
    def obter_pessoa_2(self):
        return self.pessoa_2
    
class Grafos:
    
    def __init__(self):        
        self.grafo = defaultdict(list)

    def adiciona_aresta(self, p1, p2):
        self.grafo[p1.obter_nome()].append(p2)
        self.grafo[p2.obter_nome()].append(p1)
        
    def mostrar_grafo(self, pessoa):
        for p in self.grafo[pessoa.obter_nome()]:
            print(f"Pessoa: {p.obter_nome()}")

p1 = Pessoa("Maria", 20)
p2 = Pessoa("Pedro", 30)
p3 = Pessoa("Diego", 18)
p4 = Pessoa("Carol", 25)
p5 = Pessoa("Yankee", 14)

g = Grafos()

g.adiciona_aresta(p1, p2)
g.adiciona_aresta(p1, p3)
g.adiciona_aresta(p2, p4)
g.adiciona_aresta(p4, p3)
g.adiciona_aresta(p3, p5)
g.adiciona_aresta(p5, p1)

g.mostrar_grafo(p4)