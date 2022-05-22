#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 18:25:11 2022

@author: estanislau
"""

import sys

class Grafos:
    
    def __init__(self, vertices):
        
        if vertices < 1:
            print('Erro...')
            sys.exit(1)
        
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]
        
    def adiciona_aresta(self, u, v):
        self.grafo[u - 1][v - 1] = 1
        self.grafo[v - 1][u - 1] = 1
        
    def mostrar_grafo(self):
        for i in self.grafo:
            for j in i:
                print(j, end=" ")
            print()
            
    def existe_ligacao(self, u, v):
        if self.grafo[u - 1][v - 1] == 1:
            return True
        return False
        
g = Grafos(5)

g.adiciona_aresta(1, 3)
g.adiciona_aresta(3, 4)
g.adiciona_aresta(2, 3)
g.adiciona_aresta(3, 5)
g.adiciona_aresta(4, 5)

g.mostrar_grafo()

print(g.existe_ligacao(4, 5))