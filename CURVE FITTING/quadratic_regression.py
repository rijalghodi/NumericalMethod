#Regresi Kuadrat y = ax^2 + bx + c

from numpy import*
x = input("Masukkan x (dengan spasi) : ").split(' ')
y = input("Masukkan y (dengan spasi) : ").split(' ')
matx = []

for num in x :
    matx = matx + [float(num)]
maty = []
for num in y:
    maty = maty + [float(num)]

E = array([[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]])
i = 0
while i < len(matx):
    E[0,0] = E[0,0] + (matx[i])**4
    E[0,1] = E[0,1] + (matx[i])**3
    E[0,2] = E[0,2] + (matx[i])**2
    E[1,0] = E[1,0] + (matx[i])**3
    E[1,1] = E[1,1] + (matx[i])**2
    E[1,2] = E[1,2] + (matx[i])
    E[2,0] = E[2,0] + (matx[i])**2
    E[2,1] = E[2,1] + (matx[i])
    E[1,1] = i + 1

    E[0,3] = E[0,3] + ((matx[i])**2)*maty[i]
    E[1,3] = E[1,3] + matx[i]*maty[i]
    E[2,3] = E[2,3] + maty[i]
    i = i + 1

print("\n matriks regresi :")
print(E)
print("\n Regresi Linear :")
print("y = ", str(gauss3v(E)[0]), "x^2 + ", str(gauss3v(E)[1]), "x + ", str(gauss3v(E)[2]))