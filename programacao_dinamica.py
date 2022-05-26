#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 11:27:29 2022

@author: estanislau
"""
import time
n = 35

memoria = [-1 for i in range(n)]
memoria[0] = memoria[1] = 1

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_pd(n):

    if memoria[n - 1] != -1:
        return memoria[n - 1]
    memoria[n - 1] = fibonacci_pd(n-1) + fibonacci_pd(n-2)
    return memoria[n - 1]

start_time = time.time()
print(fibonacci_pd(n))
end_time = time.time()
print(f"Tempo com pd: {(end_time-start_time):.08f} segundos")

start_time = time.time()
print(fibonacci(n))
end_time = time.time()
print(f"Tempo com pd: {(end_time-start_time):.08f} segundos")