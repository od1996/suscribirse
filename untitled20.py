# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 18:53:44 2022

@author: oscar
"""

partida1=int(input("Ingrese la 1ra partida"))
partida2=int(input("Ingrese la 2da partida"))
partida3=int(input("Ingrese la 3ra partida"))
if partida1>=partida2 and partida3>=partida2:
    resultado=partida1+partida2
else:
    resultado=partida2+partida3
print("El resultado de la calificacion es: ", resultado)

