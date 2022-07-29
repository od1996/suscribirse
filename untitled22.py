# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 17:22:16 2022

@author:oscar
"""

def burbujaordenamiento(num):
    for i in range(1,len(num)):
        for j in range(0,len(num)-i):
            if (num[j+1]<num[j]):
                auxiliar=num=[j]
                num[j]=num[j+1]
                num[j+1]=auxiliar
        print(num)
num=[2, 59, 22, 70, 97, 8, 40, 55, 91, 5, 17, 50, 80, 1, 4]                
print(num)
burbujaordenamiento(num);