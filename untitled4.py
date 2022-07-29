# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 07:10:29 2022

@author:oscar
"""

def isPrimer(num):
    numeros_primos=iter(2, 3, 5, 7, 11, 13, 17, 19)
    numeros_primos_actual=next(numeros_primos)
    resultado=[]
    cociente=None
    while cociente!=1:
        if num %numeros_primos_actual !=0:
            numeros_primos_actual=next(numeros_primos)
            continue
        resultado.append((numeros_primos_actual))
        num=cociente=num/numeros_primos_actual
    return resultado
num=int(input("Ingrese cualquier numero entero: "))
if num>0:
    factor=isPrimer(num)
    print("Factorizacion de (num):","x".join(map(str, factor)))
else:
    print("Ingrese un numero mayor que 0")
if num==1:
    factor=isPrimer(num)
    print("Factorizacion de (num):","x".join(map(str, factor)))
else:
    print("Ingrese un numero mayor que 1")
    
    