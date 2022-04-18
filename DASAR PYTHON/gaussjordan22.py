import numpy as np

baris1 = input("Masukkan baris pertama (dengan spasi) : ").split(' ')
baris2 = input("Masukkan baris kedua (dengan spasi) : ").split(' ')

A = np.array([(baris1), (baris2)], float)

print(A)
#Operasi Gauss Jordan
A[1] = A[1] - A[1,0]*A[0]/A[0,0]
A[0] = A[0] - A[0,1]*A[1]/A[1,1]

x1 = A[0,2]/A[0,0]
x2 = A[1,2]/A[1,1]

print("Solusinya adalah x1 = ", x1, " dan x2 = ", x2)