#Regresi Linear y = A . e^bx
from math import*
from numpy import*
x = input("Masukkan x (dengan spasi) : ").split(' ')
y = input("Masukkan y (dengan spasi) : ").split(' ')
matx = []
for num in x :
    matx = matx + [float(num)]
maty = []
for num in y:
    maty = maty + [float(num)]

E = array([[0,0,0],
          [0,0,0]])
i = 0

while i < len(matx):
    E[0,0] = E[0,0] + (matx[i])**2
    E[0,1] = E[0,1] + matx[i]
    E[1,0] = E[1,0] + matx[i]
    E[1,1] = i + 1

    E[0,2] = E[0,2] + matx[i]* log(maty[i])
    E[1,2] = E[1,2] + log(maty[i])
    i = i + 1
print("\n matriks regresi :")
print(E)
def gauss(A):                      #Definisi Fungsi Gauss Jordan
    A[0] = A[0]/A[0,0]
    A[1] = A[1] - A[1,0]*A[0]
    A[1] = A[1]/A[1,1]
    A[0] = A[0] - A[0,1]*A[1]
    return A[0,2], A[1,2]
b = gauss(E)[0]
A = e**(gauss(E)[1])
print("\n Regresi Eksponensial :")
print("y = ", str(A), " . e^", str(b), "x")
print(A)