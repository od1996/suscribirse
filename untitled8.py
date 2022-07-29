# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 13:55:43 2022

@author:oscar
"""
i=0
j=0
k=0
numerosprimos:[]
var2=False
import numpy as np
filas=int(input("Ingrese las dilas: "))
columnas=int(input("Ingrese las columnas: "))
matriz=np.random.randint(150,size=(filas, columnas))
print(matriz)

if matriz==2:
    print("El 2 es un numero primo")
else:
    for i in range(2, matriz):
        if (matriz % i) == 0:
            var2=True
            break
    for k in range(2, matriz+1):
        for j in range(2, int(k**0.5)+1):
            if k % j == 0:
               break
        else:
            numerosprimos.append(k)
if var2==True:
    print(matriz,"no es un primo")
else:
    print(matriz,"es un numero primo")
    
    
    
    