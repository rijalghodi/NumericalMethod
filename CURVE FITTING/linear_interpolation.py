#Interpolasi y = ax + b
from numpy import*
x1 = 1
x2 = 2
y1 = 1
y2 = 2

def gauss(A):                                                   #Definisi Fungsi Gauss Jordan
    A[0] = A[0]/A[0,0]
    A[1] = A[1] - A[1,0]*A[0]
    A[1] = A[1]/A[1,1]
    A[0] = A[0] - A[0,1]*A[1]
    return A[0,2], A[1,2]

X = array ([[x1, 1, y1],
           [x2, 1, y2]])
hasil = gauss(X)
print ("a = ", str(hasil[0]))
print ("b = ", str(hasil[1]))