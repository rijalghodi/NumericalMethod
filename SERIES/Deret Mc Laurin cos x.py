from math import*
i = 1
x = 20*pi/180
cosx = 1
suku = 1
error = 1
while error > 0.0000000000000001 :
    rasio = -(x ** 2) / ((2 * i - 1) * (2 * i))
    suku = suku * rasio
    cosxsebelum = cosx
    cosx = cosx + suku
    i += 1
    error = abs((cosx/cosxsebelum)-1)
print(cosx)
