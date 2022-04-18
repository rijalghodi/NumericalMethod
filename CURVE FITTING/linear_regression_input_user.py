'''Program ini adalah program regresi linear y = ax + b
    User menginput nilai-nilai x dan nilai-nilai y yang akan diregresi-linearkan
    lalu program akan mencari nilai a dan b 
'''


from numpy import*                                         # import semua fungsi dari modul numpy

xenon = input("Masukkan x (dengan spasi) : ").split(' ')   # inputan x dari user disimpan dalam variabel xenon 
yuli = input("Masukkan y (dengan spasi) : ").split(' ')    # inputan y dari user disimpan dalam variabel yuli

matx = []
for num in xenon :
    matx = matx + [float(num)]          # membuat list matx yang beranggotakan nilai-nilai x 
maty = []
for num in yuli:
    maty = maty + [float(num)]          # membuat list maty yang beranggotakan nilai-nilai y

A = array([[0,0,0],                     # A adalah matriks nol orde 2X3
          [0,0,0]])

i = 0                                   # iterasi awal, i = 0
while i < len(matx):                    # matriks A yang awalnya matriks nol, mulai diisi satu persatu elemennya
    A[0,0] = A[0,0] + (matx[i])**2      # baris 0 kolom 0 diberi nilai sigma x^2
    A[0,1] = A[0,1] + matx[i]           # baris 0 kolom 1 diberi nilai sigma x
    A[1,0] = A[1,0] + matx[i]           # baris 1 kolom 0 diberi nilai sigma x
    A[1,1] = i + 1                      # baris 1 kolom 1 diberi nilai n (banyak data x)

    A[0,2] = A[0,2] + matx[i]*maty[i]   # baris 0 kolom 2 diberi nilai sigma x*y
    A[1,2] = A[1,2] + maty[i]           # # baris 1 kolom 2 diberi nilai sigma y
    i = i + 1
    
print("\n matriks regresi :")
print(A)

#Eliminasi Gauss Jordan matriks A dimulai
A[0] = A[0]/A[0,0]              # Baris ke-0 dibagi elemen (0,0)
A[1] = A[1] - A[1,0]*A[0]       # Baris ke-1 dikurangi elemen (1,0) * baris ke-0
A[1] = A[1]/A[1,1]              # Baris ke-1 dibagi elemen (1,1)
A[0] = A[0] - A[0,1]*A[1]       # Baris ke-0 dikurangi elemen (0,1) * baris ke-1


print("\nRegresi Linear y = ax + b:")
print("a = ", str(A[0,2]))   # Nilai a adalah elemen (0,2) dari matriks A
print("b = ", str(A[1,2]))   # Nilai b adalah elemen (1,2) dari matriks A
