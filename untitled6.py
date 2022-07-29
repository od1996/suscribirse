# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 13:47:44 2022

@author:oscar
"""

def extraccion_del_digito_de_la_izquierda(i):
    return(int(str(i)[0]))
i=int(input("Ingrese el numero que desea extraer: "))
print("El digito es: ",extraccion_del_digito_de_la_izquierda(i))
