#Mencari akar f(x) = e^0.1x + 0.2x - 10 = 0 dengan metode bisection
from math import*
def f(x):
    nilai = e**(0.1*x) + 0.2*x - 10
    return nilai
x = 0
xbawah = 0
xatas = 30
while abs(f(x)) > 0.0001:
    x = (xatas+xbawah)/2
    if f(x) < 0:
        xbawah = x
    else:
        xatas = x
print(x)

