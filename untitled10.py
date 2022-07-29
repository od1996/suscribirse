# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 18:16:12 2022

@author: oscar
"""
def Potencias(a,b):
    res = pow(a.b)
    return res
print("--Potencias--")

while True:
    Bases = int(input("Ingrese cualquier base: "))
    
    Exponentes = int(input("Ingrese cualquier exponente: "))
    
    if Bases < 0:
        print("Error...!!!")
        
    if Exponentes < 0:
        print("Error...!!!")
        
    if Bases >= 0 and Exponentes >=0:
        break

P = Potencias(Bases,Exponentes)
print("La potenciacion es: ", P,"/n")       
    
