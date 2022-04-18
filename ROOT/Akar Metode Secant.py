#Mencari akar f(x) = e^0.1x + 0.2x - 10 = 0 dengan metode secant
from math import*
def f(x):
    f = e**(0.1*x) + 0.2*x - 10
    return f

x1 = 100  #Angka tembakan 1
x2 = 90  #Angka tembakan 2
while abs(f(x2)) > 0.0001:
    m = (f(x2)-f(x1))/(x2-x1)
    x1 = x2
    x2 = x2 - f(x2) / m
print(x2)
