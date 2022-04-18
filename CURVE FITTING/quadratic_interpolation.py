#Interpolasi y = ax^2 + bx + c
from numpy import*
x1 = 1
x2 = 2
x3 = 4
y1 = 1
y2 = 4
y3 = 16

def gauss(A):                                                   #Definisi Fungsi Gauss Jordan 3 Variable
    X[0] = X[0] / X[0][0]
    X[1] = X[1] - X[1][0] * X[0]
    X[2] = X[2] - X[2][0] * X[0]
    X[1] = X[1] / X[1][1]
    X[2] = X[2] - X[2][1] * X[1]
    X[2] = X[2] / X[2][2]
    X[1] = X[1] - X[1][2] * X[2]
    X[0] = X[0] - X[0][1] * X[1] - X[0][2] * X[2]
    return X[0,3], X[1,3], X[2,3]

X = array ([[x1**2, x1, 1, y1],
            [x2**2, x2, 1, y2],
            [x3**2, x3, 1, y3]])
hasil = gauss(X)
print ("a = ", str(hasil[0]))
print ("b = ", str(hasil[1]))
print ("c = ", str(hasil[2]))