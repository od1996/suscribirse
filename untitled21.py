# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 19:00:41 2022

@author:oscar
"""

contador=0
contadornegativo=0
contadorigual=0
while True:
    while True:
        numero1=int(input("Ingrese el 1er numero: "))
        numero2=int(input("Ingrese el 2do numero: "))
        if numero1==numero2:
           print("Error los numeros no deben ser iguales")
           contadorigual+=1
        elif numero1>0 or numero2>0:
           print("Los numeros no deben ser negativos")
           contadornegativo+=1
        else:
           break
    contador=contador+1
    print("cuantas veces",contador)
    print("cuantas veces son iguales",contadorigual)
    print("cuantas veces son negativas",contadornegativo)
    salir=int(input("Ingrese 0"))
    if salir==0:
        break