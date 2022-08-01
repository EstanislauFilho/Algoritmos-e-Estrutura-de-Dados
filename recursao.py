#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 15:02:13 2022

@author: estanislau
"""

def soma2(n):
    if n == 0:
        return 0
    return n + soma2(n - 1)
    
# print(soma2(5))

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

print(fatorial(4))