#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 20:40:04 2022

@author: estanislau
"""
import datetime

def busca_binaria(lista, chave, ini, fim):
    if ini > fim:
        return False
    
    meio = (ini + fim)//2
    
    if chave == lista[meio]:
        return True
    if chave < lista[meio]:
        return busca_binaria(lista, chave, ini, meio - 1)
    return busca_binaria(lista, chave, meio + 1, fim)


inicio = datetime.datetime.now()
print(inicio)
lista = [11, 5, 10, 20, 15, 4]
chave = 11
lista.sort()

print(busca_binaria(lista, chave, 0, len(lista) - 1))

tempo = datetime.datetime.now() - inicio

print(f"Terminou em {tempo.total_seconds():.8f} segundos.")
