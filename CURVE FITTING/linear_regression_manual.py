#Regresi Linear y = ax + b

from numpy import*
x = [1, 2, 3, 4, 5]
y = [4., 3.1, 2.6, 2.4, 2.4 ]

A = array([[0,0,0],
          [0,0,0]])
y2 = 0
i = 0
while i < len(x):
    A[0,0] = A[0,0] + (x[i])**2
    A[0,1] = A[0,1] + x[i]
    A[1,0] = A[1,0] + x[i]
    A[1,1] = i + 1

    A[0,2] = A[0,2] + x[i]*y[i]
    A[1,2] = A[1,2] + y[i]
    y2 = y2 + y[i]**2
    i = i + 1
print("\n matriks regresi :")
print(A)

A[0] = A[0]/A[0,0]
print("\nb1/", str(A[0, 0]))
print(A)
A[1] = A[1] - A[1,0]*A[0]
print("\nb2 - ", str(A[1, 0]), "b1")
print(A)
A[1] = A[1]/A[1,1]
print("\nb2/", str(A[1,1]))
print(A)
A[0] = A[0] - A[0,1]*A[1]
print("\nb1 - ", str(A[0, 1]), "b2")
print(A)
a = A[0,2]
b = A[1,2]

print("\nRegresi Linear y = ax + b:")
print("a = ", str(a), "b =", str(b))