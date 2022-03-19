# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:05:31 2022

@author: Admin
"""

a=int(input("Birinchi sonni kiriting: "))
b=int(input("Ikkinchi sonni kiriting: "))
c=int(input("Uchinchi sonni kiriting: "))
musbat=0
manfiy=0
if(a>0):
    musbat=musbat+1
else:
    manfiy=manfiy+1
if(b>0):
    musbat=musbat+1
else:
    manfiy=manfiy+1
if(c>0):
    musbat=musbat+1
else:
    manfiy=manfiy+1

print("sonlar",a,b,c)
print("Musbat sonlar : ", musbat)
print("Manfiy sonlar : ", manfiy)