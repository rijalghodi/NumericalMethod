#Mencari akar f(x) = e^0.1x + 0.2x - 10 = 0 dengan metode Newton_Raphson
from math import*
def f(x):
    y = x**2 - 4*x +3
    return y
x = 100    #nilai tembakan x
while abs(f(x)) > 0.0001:
    m = 2*x - 4
    x = x - f(x)/m
print(x)

