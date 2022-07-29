# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:25:41 2022

@author:oscar
"""
#include <iostream>
#include <iomanip>
using namespace std;
int main(){
int ent=0;
cout<<"Ingrese el numero: ";
cin>>ent;
for (int i=0;i<=ent;i++){
for(int j=ent;j>i;j--){
cout<<setw (2)<<ent-i;
}
 cout<<endl;
}
 for (int i=2;i<=ent;i++){
 for(int j=0;j<i;j++){
cout<<setw (2)<<i;
}
 cout<<endl;
}
return 0;
}
Ejercicio 5.-
#include <cmath>
#include <iostream>
using namespace std;
int main (){
double lim, x, serie=0, a=1, b=2, c=3, n;
cout << "Series en Calculadora" << endl;
cout << "\n";
cout << "Ingrese el numero de elementos: ";
cin >> lim;
cout << "ingrese el valos de x: ";
cin >> x;
n=lim*2;
for(int i=1; i<n; i+=2){
int signo =1;
if(signo % 2 != 0){
serie += pow (x, i) / (a*b*c);
}
else{
serie -= pow (x, i) / (a*b*c);
}
signo++;
a++;
b++;
c++;
}
cout << serie;
return 0
