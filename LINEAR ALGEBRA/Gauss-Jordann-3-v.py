from numpy import *
X = array([[1, 1, 1, 3],
          [1, -1, 1, -1],
          [2, 1, 1, 4]])
print (X)

print("\n b1/", str(X[0,0]))
X[0] = X[0]/X[0][0]
print(X)

print("\n b2 - " + str(X[1][0]) + "xb1")
X[1] = X[1] - X[1][0]*X[0]
print(X)

print("\n b3 - " + str(X[2][0]) + "xb1")
X[2] = X[2] - X[2][0]*X[0]
print(X)

print("\n b2/", str(X[1][1]))
X[1] = X[1]/X[1][1]
print(X)

print("\n b3 - " + str(X[2][1]) + "xb2")
X[2] = X[2] - X[2][1]*X[1]
print(X)

print("\n b3/", str(X[2][2]))
X[2] = X[2]/X[2][2]
print(X)

print("\n b2 - " + str(X[1][2]) + "xb3")
X[1] = X[1] - X[1][2]*X[2]
print(X)

print("\n b1 - " + str(X[0][1]) + "xb2 - " + str(X[0][2]) + "xb3")
X[0] = X[0] - X[0][1]*X[1] - X[0][2]*X[2]
print(X)

print("\n jadi,")
print("a = ", str(X[0][3]))
print("b = ", str(X[1][3]))
print("c = ", str(X[2][3]))
