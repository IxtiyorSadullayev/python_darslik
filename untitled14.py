# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:40:22 2022

@author: Admin
"""

a = int(input("Uch honali son kiriting: "))
birlar=a%10
yuzlar =a //100
onlar = a//10%10
print(birlar !=yuzlar !=onlar)