# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:03:38 2022

@author:oscar
"""
from math import sqrt
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n**sqrt(5))

def Fibonacci(ni, nf):
    n = 0
    valor = F(n)
    while valor <= nf:
        if ni <= valor:
            print(valor,end=(" , "))
        n += 1
        valor = F(n)
Fibonacci(1,9)










