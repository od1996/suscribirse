# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 13:01:43 2022

@author:oscar
"""
def ordenamientoBurbuja(lista):
    for j in range(len(lista)):
        for l in range(len(lista)-1):
            if lista[l]>lista[l+1]:
                auxiliar = lista[l]
                lista[l+1] = lista[l]
                lista[l] = auxiliar
    return lista
print(ordenamientoBurbuja([50, 30, 200, 52, 34, 1001, 5]))
print(ordenamientoBurbuja([50, 30, 200]))
print(ordenamientoBurbuja([50, 30, 200, 300, 5000, 1, 46, 23, 12, 76, 2]))
print(ordenamientoBurbuja(["Juan", "Ana", "Dillan", "Zulema"]))

