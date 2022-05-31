#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 20:44:12 2022

@author: estanislau
"""

# passa a lista, o início e o fim da lista
def particiona(vetor, inicio, fim):
    # o pivô é o elemento do início
    pivo = inicio
    
    for i in range(inicio + 1, fim + 1):
        if vetor[i] <= vetor[inicio]:
            pivo += 1
            vetor[i], vetor[pivo] = vetor[pivo], vetor[i]
            
    vetor[pivo], vetor[inicio] = vetor[inicio], vetor[pivo]
    return pivo


# passa a lista, o início e o fim da lista
def quick_sort(vetor, inicio, fim):
    '''
		Se o fim for maior que o iníco, então
		eu calculo a posição do pivô utilizando
		 a função particiona
	'''
    if fim > inicio:
        # separa os dados em duas partições
        pivo = particiona(vetor, inicio, fim)
        
        '''
			Tendo o pivô, chama a função duas
			vezes para cada partição, a primeira
			dos elementos que estão antes do pivô
			e a segunda é a dos elementos que estão
			depois do pivô
		'''
        vetor = quick_sort(vetor, inicio, pivo - 1)
        vetor = quick_sort(vetor, pivo + 1, fim)
    return vetor

vetor = [3, 15, 7, 12, 17, 1, 26, 4]

vetor = quick_sort(vetor, 0, len(vetor) - 1)

print(vetor)