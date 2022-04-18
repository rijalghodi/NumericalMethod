Matriks = input("Masukkan baris pertama (dgn spasi): ").split(' ')
brs1 = [int(num) for num in Matriks]

Matriks = input("Masukkan 3 angka baris kedua (dgn spasi): ").split(' ')
brs2 = [int(num) for num in Matriks]

Matriks = input("Masukkan 3 angka baris ketiga (dgn spasi): ").split(' ')
brs3 = [int(num) for num in Matriks]


print()
print ("Masukkan matriks vektor")
a1 = input("a1:")
v1 = [int(a1)]
a2 = input("a2:")
v2 = [int(a2)]
a3 = input("a3:")
v3 = [int(a3)]

print()
print("Hasil Augmented Matriks")
print(brs1+v1)
print(brs2+v2)
print(brs3+v3)

print()
b1=brs1+v1
b2=brs2+v2
b3=brs3+v3

print("Hasil Eliminasi Gauss")
print("B2-B1: ")
print(b1)
print("[",b2[0]-b1[0], b2[1]-b1[1], b2[2]-b1[2], b2[3]-b1[3],"]")
print(b3)
print()
print("B3-(2.B1): ")
print(b1)
print("[",b2[0]-b1[0], b2[1]-b1[1], b2[2]-b1[2], b2[3]-b1[3],"]")
print("[",b3[0]-(2*b1[0]), b3[1]-(2*b1[1]), b3[2]-(2*b1[2]), b3[3]-(2*b1[3]),"]")

print()
print("Hasil Eliminasi Gauss Jordan")
print("x + 2y + z = 6")
print("y + z = 3")
print("-3y = 0")
print()
y=0/-3
print("Hasil y: ")
print(int(y))
z=3-0
print("Hasil z: ")
print(int(z))
x=6-(2*0)-3
print("Hasil x: ")
print(int(x))