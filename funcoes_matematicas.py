#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:04:37 2022

@author: estanislau
"""
import math

def fatorial(n):
    if n == 0:
        return 1
    return (n * fatorial(n-1))

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def somatorio(n):
    return ((n*(n+1))/2)


fatorial_lambda = lambda n: n * fatorial(n-1) if n > 1 else 1


print(fatorial(5))
print(fatorial_lambda(5))
print(fibonacci(6))

print("\nFunções Math")
print(math.log10(10))
print(math.cos(0))
print(math.sin(30))
print(math.sin(90))
print(math.sqrt(25))


print()
print(somatorio(10))