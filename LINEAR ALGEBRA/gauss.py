from numpy import*
def gauss3v(X):                                                   #Definisi Fungsi Gauss Jordan 3 Variable
    X[0] = X[0] / X[0][0]
    X[1] = X[1] - X[1][0] * X[0]
    X[2] = X[2] - X[2][0] * X[0]

    X[1] = X[1] / X[1][1]
    X[2] = X[2] - X[2][1] * X[1]

    X[2] = X[2] / X[2][2]

    X[1] = X[1] - X[1][2] * X[2]
    X[0] = X[0] - X[0][1] * X[1] - X[0][2] * X[2]
    return X[0,3], X[1,3], X[2,3]

def gauss2v(A):
    A[0] = A[0] / A[0, 0]
    A[1] = A[1] - A[1, 0] * A[0]
    A[1] = A[1] / A[1, 1]
    A[0] = A[0] - A[0, 1] * A[1]
    return A[0, 2], A[1, 2]

