# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 11:50:31 2022

@author:oscar
"""
from math import sqrt
m=int(input("Ingrese un numero valor en m: "))
n=int(input("Ingrese un numero valor en n: "))
ñ=int(input("Ingrese un numero valor en ñ: "))
o=(n*n)-4*m*ñ
if m==0:
    print("")
    print("Division para cero")
else:
    if o<0:
        print("")
        print("Raiz negativa")
    else:
        raiz=sqrt(o)
        n1=(-n + raiz)/(2*m)
        if o !=0:
            n2=(-n - raiz)/(2*m)
            print("")
            print("Dos soluciones: ")
            print("n1=",n1)
            print("n2=",n2)
        else:
            print("")
            print("Unica solucion:")
            print("n=",n1)
            

