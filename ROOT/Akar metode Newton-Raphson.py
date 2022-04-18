#Mencari akar f(x) = e^0.1x + 0.2x - 10 = 0 dengan metode Newton_Raphson
from math import*
def f(x):
    f = -x**4 - 4*x**3 + 2*x**2 + 16*x + 16
    return f
x = -100  #nilai tembakan x
while abs(f(x)) > 0.001:
    m = (f(x+0.01)-f(x))/0.01
    x = x - f(x)/m

print(x)

