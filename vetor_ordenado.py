#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:53:54 2022

@author: estanislau
"""
import time
import numpy as np

class Vetor_Ordenado:
    
    def __init__(self, tamanho_vetor):    
        self.tamanho_vetor = tamanho_vetor
        self.ultima_posicao_vetor = -1
        self.vetor = np.empty(self.tamanho_vetor, dtype=int)
    
    def imprime(self):
        if self.ultima_posicao_vetor == -1:
            print("vetor vazio!")
        else:
            for i in range(self.ultima_posicao_vetor+1):
                print(f"Posição vetor: {i} \tValor: {self.vetor[i]}")
         
    # Análise Assintótica: O(n)
    def inserir_valor(self, valor):
        # Verifica se o vetor já totalmente preenchido
        if self.ultima_posicao_vetor == (self.tamanho_vetor - 1):   
            print("Capacidade máxima atingida")
            return
        
         # realiza uma pesquisa linear no vetor para verificar se o valor pesquisado é maior que qual elemento da lista
        posicao = 0
        for i in range(self.ultima_posicao_vetor+1):   
            posicao = i
            if self.vetor[i] > valor:
                break
            
            # se percorrer o vetor inteiro e estiver na última posição do vetor, a variavel posicao deve ser incrementada
            # para ir para o próximo slot vazio do vetor
            if i == self.ultima_posicao_vetor:
                posicao = i + 1
            
        # Realiza um shift nos outros elementos do vetor quando descobrir onde inserir o novo valor no vetor
        # Remaneja os valores
        x = self.ultima_posicao_vetor 
        while x >= posicao:
            self.vetor[x + 1] = self.vetor[x]
            x -= 1
            
        # faz a inserção do valor desejado na posição em que este valor vá fazer com que a lista continue ordenada.
        self.vetor[posicao] = valor
        self.ultima_posicao_vetor += 1
        
        
    def pesquisa_valor(self, valor):
        for i in range(self.ultima_posicao_vetor + 1):
            if valor < self.vetor[i]:
                # se o valor pesquisado for menor que o primeiro elemento do vetor, então esse valor não está contido no vetor
                return -1
            if valor == self.vetor[i]:
                # se o valor pesquisado for igual ao elemento do vetor na posição i, então encontrou o valor
                return i
            if i == self.ultima_posicao_vetor:
                # se i pecorreu todo o vetor até a ultima posição do vetor e não encontrou o valor, 
                # então esse valor não está contido no vetor
                return -1
            
    
    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao_vetor 
        
        while True:
            # faz uma divisão da lista pela metade
            posicao_atual = int((limite_inferior + limite_superior)/2) 
            
            if valor == self.vetor[posicao_atual]:
                # se o valor pesquisado estiver na metade exata da lista, retorna a posição
                return posicao_atual
            
            elif limite_inferior > limite_superior:
                # se o limite inferior for maior que o limite superior, significa que que não encontrou o elemento
                return -1
            
            else:
                if valor > self.vetor[posicao_atual]:
                    # se o valor pesquisado for maior do que valor atual da lista em sua metade, então o valor pode
                    # estar mais a direita da lista
                    limite_inferior = posicao_atual + 1
                else:
                    # se o valor pesquisado for menor do que valor atual da lista em sua metade, então o valor pode
                    # estar mais a esquerda da lista
                    limite_superior = posicao_atual - 1
                


    def excluir_valor(self, valor):
        # faz a pesquisa pela posicao do valor no vetor
        posicao = self.pesquisa_valor(valor)
        if posicao == -1:
            # se o valor não for encontrado no vetor então retorna -1
            return -1
        else:
            # se o valor foi encontrado no vetor, então faça a reorganização dos demais valores do vetor
            # substituindo o valor encontrado no vetor pelos proximos valores do vetor
            for i in range(posicao, self.ultima_posicao_vetor):
                self.vetor[i] = self.vetor[i + 1]
            self.ultima_posicao_vetor -= 1
    
if __name__ == "__main__":
    tempo_inicial = time.time()
    vetor = Vetor_Ordenado(10)
    vetor.imprime()
    
    vetor.inserir_valor(15)
    vetor.inserir_valor(15)
    vetor.inserir_valor(15)
    vetor.inserir_valor(7)
    vetor.inserir_valor(97)
    vetor.inserir_valor(2)
    
    vetor.imprime()
    
    print(vetor.pesquisa_valor(97))
    
    vetor.excluir_valor(15)
    
    vetor.imprime()
    
    print(vetor.pesquisa_valor(97))
    print(vetor.pesquisa_binaria(9))
    
    tempo_final = time.time()
    print(f"Tempo de execução: {(tempo_final-tempo_inicial):.8f} segundos.")
    