#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 19:42:32 2022

@author: estanislau
"""

import sys
import time
import random

class Gerador_Grafos:
    
    def __init__(self, vertices):
        
        if vertices < 1:
            print('Erro...')
            sys.exit(1)
        
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
        self.custos = {}
        
    def gerar_grafo(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j :
                    if (i, j) and (j, i) not in self.custos: 
                        custo = random.randint(1, 100)
                        self.custos[(i, j)] = custo
                        self.custos[(j, i)] = custo
                    self.grafo[i].append(j)
        
    def mostrar_grafo(self):
        for i in range(self.vertices):
            print(f"Adjacentes de {i} -> ", end=" ")
            for j in self.grafo[i]:
                print(f"{j} (custo: {self.custos[i, j]})", end=" ")
            print()
            
    def pvc_random(self, iteracoes):
        
        melhor_circuito = []
        melhor_custo = None
        
        def gerar_circuito(melhor_circuito, melhor_custo):
            
            vertices = [i for i in range(1, self.vertices)]
            circuito = [0]
            custo_circuito = 0
            
            while(len(vertices) > 0):
                e = random.choice(vertices)
                vertices.remove(e)
                custo_circuito += self.custos[(circuito[-1], e)]
                circuito.append(e)
            
            custo_circuito += self.custos[(circuito[-1], 0)]
            
            if melhor_custo is None:
                melhor_circuito = circuito[:]
                melhor_custo = custo_circuito
            else:
                if custo_circuito < melhor_custo:
                    melhor_circuito = circuito[:]
                    melhor_custo = custo_circuito
                    

            return melhor_circuito, melhor_custo
          
        for i in range(iteracoes):
            melhor_circuito, melhor_custo = gerar_circuito(melhor_circuito, melhor_custo)
            print(f"Melhor circuito: {melhor_circuito} Custo: {melhor_custo}")
            time.sleep(1)
            
gerador = Gerador_Grafos(5)
gerador.gerar_grafo()
gerador.mostrar_grafo()
gerador.pvc_random(10)