#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 21:07:58 2022

@author: estanislau
"""

def fatorial(n):
    if n == 0:
        return 1
    return (n * fatorial(n-1))

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))