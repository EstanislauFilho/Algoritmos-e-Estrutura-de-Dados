#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 18:50:30 2022

@author: estanislau
"""

import sys

class Grafos:
    
    def __init__(self, vertices):
        
        if vertices < 1:
            print('Erro...')
            sys.exit(1)
        
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
        
    def adiciona_aresta(self, u, v):
        self.grafo[u - 1].append(v - 1)
        
    def mostrar_grafo(self):
        for i in range(self.vertices):
            print("%d: "%(i+1), end=" ")
            for j in self.grafo[i]:
                print("%d "%(j + 1), end=" ")
            print()
        
        
g = Grafos(5)

g.adiciona_aresta(1, 2)
g.adiciona_aresta(4, 1)
g.adiciona_aresta(2, 3)
g.adiciona_aresta(2, 5)
g.adiciona_aresta(5, 3)

g.mostrar_grafo()
