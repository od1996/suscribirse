# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
""" 

#Evaluar el valor de suma
suma=0
#Evaluar el valor del promedio
promedio=0
#Incluir una funcion para evaluar el N de tablas
for n in  range (1,20):
    #Area para el formato de la tabla
    print(" ")
    #Nota para el formato de la tabla
    print("La tabla del N: ",n)
    #Area para el formato de la tabla
    print(" ")
    #Evaluar el valor del par
    par=0
    #Evaluar el valor del impar
    impar=0
    #Incluir un for para determinar todas las veces que se multiplicaran las tablas
    for i in range (1,20):
        #Ejecucion para sacar el valor de la multiplicacion 
        multi=i*n
        #Ejecucion para sacar la suma de todos los valores de la multiplicacion
        suma+=multi
        #Incluir para sacar el promedio de cada una de la tabla
        promedio=suma//19
        #Dimension de la tabla de multiplicar
        print(i,"x",n,"=",multi)
        #Incluir un if para determinar el valor de la multiplicacion si es par o impar
        if multi/2==0:
            #si es par
            par=par+1
        #sino
        else:
            #es impar
            impar=impar+1
    #Mensaje con la suma total de cada una de las tablas
    print("La suma de los numeros es",suma)
    #Mensaje con el promedio total de cada una de las tablas
    print("El promedio de los numeros es",promedio)
    #Mensaje con la cantidad de los numeros pares que existen en cada una de las tablas
    print("Num",par,"numeros pares")
    #Mensaje con la cantidad de los numeros impares que existen en cada una de las tablas
    print("Num",impar,"numeros impares")
    #Formato para la tabla 
    print(" ")
    break
