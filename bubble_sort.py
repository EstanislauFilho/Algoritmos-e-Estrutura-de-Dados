#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 21:12:32 2022

@author: estanislau
"""


def bubble_sort(v):

	len_v = len(v)

	for i in range(len_v - 1, 0, -1):
		swapped = False
		for j in range(i):
			if v[j] > v[j + 1]:
				v[j], v[j + 1] = v[j + 1], v[j]
				swapped = True
		if not swapped:
			break


v = [23, 6, 7, 1, 19, 2, 18]
bubble_sort(v)
print(v)


