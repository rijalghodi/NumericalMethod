i = 1
x = 0.5
ex = 1
suku = 1
error = 1
while error > 0.0000000000000001 :
    rasio = x / i
    suku = suku * rasio
    exsebelum = ex
    ex = ex + suku
    i += 1
    error = abs((ex/exsebelum)-1)
print(ex)
