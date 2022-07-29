# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 07:31:49 2022

@author:oscar
"""

import math
def isPrime(num):
 for a in range(3,int(math.sqrt(num))+1,2):
  if num%a==0:
   return False
 return True
def listofPrimes(limit):
 print(2)
 for b in range(3,limit+1,2):
  if isPrime(b):
   print(b)
listofPrimes()
