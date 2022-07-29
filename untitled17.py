# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 18:43:40 2022

@author: osacar
"""

acl=int("Ingrese el # de ACL: ")
if acl>=1 and acl<=99:
    print("Es un ACL estandar")
elif acl>=100 and acl<=199:
    print("Es un ACL extendida")
else:
    print("El # ingresado no es de un ACL")
    