# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:18:20 2020

@author: zalgh
"""
from math import*
import matplotlib.pyplot as mt
from numpy import*
barisan = []
waktu = []
t=-6   
while t < 12:
    suku = 0
    for n in range (1,6):
        suku = suku + (-2/n)*sin(n*t)
    barisan = barisan + [3.14 + suku]
    waktu = waktu + [t]
    t = t+0.01
mt.plot(waktu,barisan)
mt.show