# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 20:21:58 2022

@author:oscar
"""

contador1=0
contador2=0
suma=0
promedio=0
lista=[]
for i in range(1,6):
    valor=float(input("Ingrese la estatura: "))
    suma+=valor
    lista.append(valor)
promedio=suma/5
print("El promedio total es: ",promedio)
for j in range(5):
    if lista[j]>promedio:
        contador1+=1
    else:
        contador2+=1
print("Hay",contador1,"mayor que el promedio")
print("Hay",contador2,"Menor que el promedio")
