def f (x,y):
    f = (x**2)*(y**2)
    return f

def fdy(x,y):                                   # df/dy
    b = (f(x, y*(1+0.0001))-f(x,y))/(y*0.0001)
    return b
print(fdy(1,1))