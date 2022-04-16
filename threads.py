#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 18:55:07 2022

@author: estanislau
"""
import time

from threading import Thread

def my_func(i):
    print(f'Iniciando a thread {i}\n')
    time.sleep(3)
    print(f'Finalizando a thread {i}\n')
    
for i in range(10):
    t = Thread(target=my_func, args = (i,))
    t.start()