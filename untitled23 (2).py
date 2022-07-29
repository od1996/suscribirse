# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:58:44 2022

@author:oscar
"""

matrix=[[int() for i in range(4)]for j in range (4)]
#SE USA DOS FOR UNA PARA LAS FILAS Y OTRA PARA LAS COLUMNAS
for filas in range(4):
    for columnas in range(4):
        #LLENAR LA MATRIZ CON LOS VALORES INGRESADOS
        valor=int(input("Ingrese el valor: "))
        matrix[filas][columnas] = valor
for i in range(4):
    print("|", end=" ")
    for j in range(4):
        print(matrix[i][j], " | ", end=" ")
        
    print("\n")
print(matrix)
        