# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 11:57:06 2022

@author:oscar
"""
N = int(input("Ingrese un numero entero: "))
j = 0
res = 0
print("\n--Sucesion de numeros enteros--")
while j < N:
    l = pow(2,N)
    res += 1
    N-= 1
print("El resultado de la serie es: ",res)