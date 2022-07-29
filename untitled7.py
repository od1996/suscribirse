# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 13:51:06 2022

@author:oscar
"""
def Numeromayor(a,b,c):
    if a > b and c:
        print(" ")
        print("El numero mayor es: ",a)
    if b > a and c:
        print(" ")
        print("El numero mayor es: ",b)
    if c > a and b:
        print(" ")
        print("El numero mayor es: ",c)
        
a=int(input("Ingrese un valor en A: "))
b=int(input("Ingrese un valor en B: "))
c=int(input("Ingrese un valor en C: "))
print(Numeromayor(a, b, c))        
        
    