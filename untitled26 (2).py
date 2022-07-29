# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 17:29:30 2022

@author:oscar
"""
def keyw(**datos):
    print("\nTipo de datos del argumento: ",type(datos))
    for key, value in datos.items():
        print("{} is {}",format(key,value))
keyw(Firstname="Jorge",
     Lastname="Morocho",
     Age=18,
     Phone=172354981)
keyw(Firstname="Anderson",
     Lastname="Quelal",
     Email="elpollitopio45@gmail.com",
     Country="Ecuador",
     Age=18,
     Phone=455521225)


