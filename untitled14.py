# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:12:07 2022

@author:oscar
"""
from math import factorial
def SerieIlimitado(n,Ilimitado):
    suma=n
    for a in range(0,Ilimitado):
        valores=pow(n,a)/factorial(n)
        suma+=valores
        print("Iteracion: ",n,"\nValores: ",valores,"\nsuma: ",suma)
print("Serie Ilimitada")
n=int(input("Escriba el valor de n: "))
while True:
    Ilimitado=int(input("Escriba un numero entero positivo: "))
    if Ilimitado > 0:
        break
SerieIlimitado(n, Ilimitado)