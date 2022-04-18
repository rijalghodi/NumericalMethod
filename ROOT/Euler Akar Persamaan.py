#Ini program untuk mencari akar persamaan 2^x + x = 0 (pertanyaan dari raihan nur rasyid di sms 1)
from math import*
i = 1
x = -1
y = -0.5
while y<0 :
    xsebelum = x
    x = x + 0.001
    m = 2 ** x * log(2, e)
    y = y + m*0.001
print(y)



