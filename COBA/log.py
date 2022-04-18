# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:38:46 2020

@author: zalgh
"""
a = input("a = ")

b = input("b = ")

ans = 0

while int(a)**ans < abs(int(b)):
    ans = ans+0.1

print(ans-0.1)