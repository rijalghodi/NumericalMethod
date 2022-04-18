# Fungsi Rasional: y = ax+b/x+c
# diubah menjadi y = Ax + B - Cxy
# di mana A = a/c, B = b/c, dan C = 1/c

from numpy import*
x = [1, 2, 3, 4]
y = [2, 3/2, 4/3, 5/4]

E = array([[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]])
i = 0
while i < len(x):
    E[0,0] = E[0,0] + (x[i])**2
    E[0,1] = E[0,1] + x[i]
    E[0,2] = E[0,2] + ((x[i])**2)*(y[i])
    E[0,3] = E[0,3] + x[i]*y[i]
    E[1,0] = E[1,0] + x[i]
    E[1,1] = i + 1
    E[1,2] = E[1,2] + x[i]*y[i]
    E[1,3] = E[1,3] + y[i]
    E[2,0] = E[2,0] + (x[i]**2)*y[i]
    E[2,1] = E[2,1] + x[i]*y[i]
    E[2,2] = E[2,2] + (x[i]**2)*(y[i]**2)
    E[2,3] = E[2,3] + x[i]*y[i]**2
    i = i + 1

def gauss3v(X):                                                   #Definisi Fungsi Gauss Jordan 3 Variable
    X[0] = X[0] / X[0,0]
    X[1] = X[1] - X[1][0] * X[0]
    X[2] = X[2] - X[2][0] * X[0]

    X[1] = X[1] / X[1,1]
    X[2] = X[2] - X[2][1] * X[1]

    X[2] = X[2] / X[2,2]

    X[1] = X[1] - X[1][2] * X[2]
    X[0] = X[0] - X[0][1] * X[1] - X[0][2] * X[2]
    return X[0,3], X[1,3], X[2,3]

A = gauss3v(E)[0]
B = gauss3v(E)[1]
C = gauss3v(E)[2]

print("A = ", str(A), ", B = ", str(B), ", C = ", str(C))

c = 1/C
b = B*c
a = A*c
print("a = ", str(a), ", b = ", str(b), ", c = ", str(c))