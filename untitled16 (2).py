# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:24:34 2022

@author:oscar
"""
#include<iostream>
using namespace std;
int main(){
double x=0;
double anios=0;
double interes=0;
cout<<"Ingrese el dinero inicial: ";
cin>>x;
while ((x<500)||(x<=0)){
cout<<"Ingrese el dinero inicial: ";
cin>>x;
}
cout<<"Ingrese el tiempo (anios): ";
cin>>anios;
cout<<"Ingrese el interes: ";
cin>>interes;
while ((interes>10)||(interes<=0)){
cout<<"Ingrese el interes: ";
 cin>>interes;
}
int meses=anios*12;
for (int i=1;i<=meses;i++){
x=(x*(interes/100))+x;
}
cout<<"Total de la poliza es: "<<x<<endl;
return 0;
}
