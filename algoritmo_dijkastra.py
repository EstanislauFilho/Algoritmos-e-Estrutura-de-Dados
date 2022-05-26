#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 21:54:30 2022

@author: estanislau
"""

import heapq
from collections import defaultdict

class Fila_De_Prioridade:
    
    def __init__(self):
        self.fila_de_prioridade = [] 
        self._indice = 0
        
    def inserir_na_fila(self, objeto, prioridade):
        heapq.heappush(self.fila_de_prioridade, (-prioridade, self._indice, objeto))
        self._indice += 1
        
    def retirar_da_fila(self):
        if len(self.fila_de_prioridade) > 0:
            return heapq.heappop(self.fila_de_prioridade)[-1]
            
            
    def mostrar(self):
        print(self.fila_de_prioridade)
        
    def obter_tamanho_fila(self): 
        return len(self.fila_de_prioridade)
    
    
class Grafos:
    
    def __init__(self):        
        self.grafo = defaultdict(list)
        self.vertices = {}
        
    def adiciona_aresta(self, fonte, destino, custo):
        self.grafo[fonte].append((destino, custo))
        self.vertices[fonte] = fonte
        self.vertices[destino] = destino 
        
    def mostrar_grafo(self, fonte):
        for f in self.grafo[fonte]:
            print(f"Pessoa: {f.obter_nome()}")
            
    def dijkstra(self, fonte, destino):
        numero_de_vertices = len(self.vertices)
        p = [None for i in range(numero_de_vertices)]

        p[fonte] = 0
        
        min_heap = Fila_De_Prioridade() # constroi a min_heap
            
        min_heap.inserir_na_fila(fonte, 0) # insere a origem na min_heap
        
        while min_heap.obter_tamanho_fila() > 0: # enquanto o tamanho da fila for maior que 0
            u = min_heap.retirar_da_fila() # remo da fila de prioridades
            for aresta in self.grafo[u]: # percorre os adjacentes de 'u'
                v, custo = aresta # obtém o vertice adjacente e o custo
                
                if p[v] is None or p[v] > p[u] + custo: # relaxamento
                    p[v] = p[u] + custo # atualiza a estimativa de custo
                    min_heap.inserir_na_fila(v, p[v]) # insere na fila de prioridades
        
        return p[destino] # retorna o custo do menor caminho
        
g = Grafos()

g.adiciona_aresta(0, 1, 1)
g.adiciona_aresta(0, 3, 3)
g.adiciona_aresta(0, 4, 10)
g.adiciona_aresta(1, 2, 5)
g.adiciona_aresta(2, 4, 1)
g.adiciona_aresta(3, 2, 2)
g.adiciona_aresta(3, 4, 6)

    
print(g.dijkstra(0, 4))
