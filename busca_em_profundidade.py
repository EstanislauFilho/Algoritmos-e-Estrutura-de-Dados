#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 19:40:09 2022

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
        self.visitados = [False] * self.vertices
        
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
    
    def dfs(self, u):
        self.visitados[u - 1] = True
        print("%d visitado "%u)
        for i in range(1, self.vertices + 1):
            if self.grafo[u - 1][i - 1] == 1 and self.visitados[i - 1] == False:
                self.dfs(i)
        
g = Grafos(5)

g.adiciona_aresta(1, 4)
g.adiciona_aresta(4, 2)
g.adiciona_aresta(4, 5)
g.adiciona_aresta(2, 5)
g.adiciona_aresta(5, 3)

g.dfs(1)
