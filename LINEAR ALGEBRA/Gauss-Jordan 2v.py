from numpy import*
def Gauss(A):                   #Definisi Fungsi Gauss Jordan
    A[0] = A[0]/A[0,0]
    A[1] = A[1] - A[1,0]*A[0]
    A[1] = A[1]/A[1,1]
    A[0] = A[0] - A[0,1]*A[1]
    return A[0,2], A[1,2]

A = array ([[1., 2., 15.],
            [3., 4., 35.]])
print(Gauss(A))