# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 19:49:34 2022

@author:oscar
"""

hora=int(input("Ingrese una hora hh: "))
minutos=int(input("Ingrese un minuto mm: "))
segundos=int(input("Ingrese los segundos ss: "))
error=False
#Validacion de hora
if hora>23 or hora<0:
    print("El dato de la hora no es correcta")
    error=True 
#Validacion de minutos
if minutos<0 or minutos>59:
    print("El dato de los minutos no es correcta")
    error=True
#Validacion de segundos
if segundos<0 or segundos>59:
    print("El dato de los segundos no es correcta")
if error==False:
    print("Puede continuar")
    segundos2=int(input("Ingrese el valor de segundos extras: "))
if segundos2<0:
    print("EL valor de los segundos extras no son correctas")
else:
    print("Puede continuar")
    ensegundos=(hora*3600)+(minutos*60)+segundos
    suma=segundos2+ensegundos
    hh=int(suma/3600)
    mm=int((suma/60)-(hh*60))
    ss=int((suma-(mm*60)-(hh*3600)))
    print(hh,mm,ss)
    


