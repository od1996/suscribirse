# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:16:35 2022

@author:oscar
"""
#include <iostream>
using namespace std;
int main(){
cout << "NUMEROS ELEVADOS AL CUADRADO" << endl;
int a, b, n;
cout << "\nIngrese un numero: ";
cin >> n;
for (int i = 1; i <= 100; i++){
int j = 1; a = 1; b = 1;
while (j < i){
a = a + 2;
b = b + a;
j++;
}
cout << i << " ^ 2 = "<< b << endl;
}
return 0;
}