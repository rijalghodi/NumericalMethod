
from math import*
import matplotlib.pyplot as mt
from numpy import*
barisan = []
waktu = []
t=-6   
while t < 12:
    suku = 0
    for n in range (1,6):
        suku = suku + (-8/3.14)*(1/(n**2 -1))*cos(2*n*t)
    barisan = barisan + [2/3.14 + suku]
    waktu = waktu + [t]
    t = t+0.01
mt.plot(waktu,barisan)
mt.show