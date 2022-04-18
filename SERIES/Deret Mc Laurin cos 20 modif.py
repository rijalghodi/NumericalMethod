from math import*
def faktorial(j):
    fac = 1
    k = 1
    while k <= j :
        fac = fac * k
        k += 1
    return fac

x = int(input("sin "))
n = int(input("Sampai berapa keakuratan desimal? "))
x = x*pi/180
i = 0
sign = -1
nilai = 0
suku = 1
while abs(suku) >= (10**(-(n+1))) :
    if i%2 == 1 :
        suku = (x**i)*sign/faktorial(i)
        nilai = nilai + suku
        i += 1
    else :
        sign = sign*(-1)
        i += 1
print(round(nilai,n))

    

