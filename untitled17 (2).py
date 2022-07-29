# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:25:12 2022

@author:oscar
"""
#include<iostream>
#include <iomanip>
using namespace std;
int main(){
double paquetes=0,te=0,ping=0;
cout<<"Ingrese el tamanio de lo que consta el paquete: ";
cin>>paquetes;
cout<<"Tamanio maximo de ventana: ";
cin>>te;
for(int i=0;i<=10;i++){
for(int j=1;j<=te;j++){
if(i==0){
cout << setw (10)<<j*paquetes;
}
if (i==1){
cout<<"10";
ping=paquetes*j/10;
 cout <<setw (8) <<setprecision(1) <<fixed<<ping;
}
if(i==2){
cout<<"20";
ping=paquetes*j/20;
 cout << setw (8) << setprecision(1) << fixed<<ping;
}
 if(i==3){
 cout<<"30";
 ping=paquetes*j/30;
cout << setw (8) << setprecision(1) << fixed<<ping;
 }
 if (i==4){
 cout<<"40";
 ping=paquetes*j/40;
cout << setw (8) << setprecision(1) << fixed<<ping;
}
 if (i==5){
 cout<<"50";
 ping=paquetes*j/50;
 cout << setw (8) << setprecision(1) << fixed<<ping;
}
 if (i==6){
 cout<<"60";
 ping=paquetes*j/60;
 cout << setw (8) << setprecision(1) << fixed<<ping;
} 
 if (i==7){
 cout<<"70";
 ping=paquetes*j/70;
 cout << setw (8) << setprecision(1) << fixed<<ping;
}
 if (i==8){
 cout<<"80";
 ping=paquetes*j/80;
 cout << setw (8) << setprecision(1) << fixed<<ping;
 }
 if (i==9){
 cout<<"90";
 ping=paquetes*j/90;
 cout << setw (8) << setprecision(1) << fixed<<ping;
 }
 if (i==10){
 cout<<"100";
 ping=paquetes*j/100;
 cout << setw (7) << setprecision(1) << fixed<<ping;
 }
 }
 cout<<endl;
}
return 0;
}

