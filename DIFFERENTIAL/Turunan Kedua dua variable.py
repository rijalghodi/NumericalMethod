#df/dxdy pada (1,2) di mana f = x^2*y^2 Menggunakan metode forward
from math import*
def f (x,y):
    f = (e**(2*x*y)) + (y**(3*x))
    return f

def fdx(x,y):                                   # df/dx
    a = (f(x*(1+0.0001),y)-f(x,y))/(x*0.0001)
    return a

def fdy(x,y):                                   # df/dy
    b = (f(x, y*(1+0.0001))-f(x,y))/(y*0.0001)
    return b

def fdxx (x,y):                                 # df/dxx
    a = (fdx(x*(1+0.0001),y)-fdx(x,y))/(x*0.0001)
    return a

def fdyy (x,y):                                 # df/dyy
    a = (fdy(x, y*(1+0.0001))-fdy(x,y))/(y*0.0001)
    return a

def fdxy (x,y):                                 # df/dxy
    a = (fdx(x, y*(1+0.0001))-fdx(x,y))/(y*0.0001)
    return a

def fdyx (x,y):                                 # df/dyx
    a = (fdy(x*(1+0.0001),y)-fdy(x,y))/(x*0.0001)
    return a

print(fdxy(1,1))
print(fdyx(1,1))