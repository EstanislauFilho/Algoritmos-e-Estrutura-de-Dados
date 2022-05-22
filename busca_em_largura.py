#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 20:24:17 2022

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
    
    def bfs(self, v):
        self.visitados[v - 1] = True # marca v como visitado
        fila = [v - 1] # insere v na fila
        
        while(len(fila) > 0): # enquanto a fila não for vazia
            
            v = fila[0] # obtem o primeiro elemento da fila
            
            for u in range(self.vertices): # para cada vertice u adjacente a v
                if self.grafo[v][u] == 1: # verifica se existe conexão
                    if self.visitados[u] == False: # verifica se u não foi visitado
                        self.visitados[u] = True # marca u como visitado
                        fila.append(u)
                        print("%d visitado "%(u+1))
            fila.pop(0)
            
            
g = Grafos(10)

g.adiciona_aresta(1, 2)
g.adiciona_aresta(1, 3)
g.adiciona_aresta(1, 4)
g.adiciona_aresta(2, 5)
g.adiciona_aresta(3, 6)
g.adiciona_aresta(3, 7)
g.adiciona_aresta(4, 8)
g.adiciona_aresta(5, 9)
g.adiciona_aresta(6, 10)

g.bfs(1)
