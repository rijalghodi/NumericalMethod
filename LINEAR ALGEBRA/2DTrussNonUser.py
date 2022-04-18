"""
Created on Wed May 12 15:40:31 2021
2 D Truss Analysis Using Finite Element Analysis 
@author: Rijal Ghodi
"""

import numpy as np
from math import*



'''----------------------------------------------------------------------------
1. Mendaftar data setiap element pada 2D truss model
----------------------------------------------------------------------------'''

jml_elemen = 6 #Banyak elemen truss
jml_node = 5   #Banyak node

luas = np.array ([8, 8 , 8, 8, 8, 8])                         #Luas cross section setiap elemen
young = np.array ([1.9e6, 1.9e6, 1.9e6, 1.9e6, 1.9e6, 1.9e6]) #modulus young setiap elemen
panjang = np.array([36, 50.9, 36 , 36 , 50.9, 36])            #panjang tiap elemen

nodei = np.array([1, 2, 3, 2, 2, 4]) #index node-kiri setiap elemen
nodej = np.array([2, 3, 4, 4, 5, 5]) #index node-kanan setiap elemen

deg = pi/180
sudut = np.array([0*deg, 135*deg, 0*deg, 90*deg, 45*deg, 0*deg]) #sudut setiap elemen thd smb x positif




'''----------------------------------------------------------------------------
2. Mendaftar gaya eksternal yang membebani node-node
----------------------------------------------------------------------------'''

force = np.array([[0 , 0, 0, 0, 0, 0, 0, -500, 0, -500]])
#Note: gaya disusun dengan urutan fxi, fyi, fx(i+1), fy(i+1), dst

    


'''----------------------------------------------------------------------------
3. Menentukan Matriks Stiffness
----------------------------------------------------------------------------'''

# 3.a. Mengonversi karakteristik elemen (A, E, L) menjadi stiffness (k)
stiff = luas*young/panjang     
print("\nStiffness\n", stiff)

# 3.b. Membuat fungsi mat_stiff_lokal, yang memiliki luaran berupa matriks stiffness lokal 
#      untuk input sudut dan stiffness tertentu
def mat_stiff_lokal (teta, stiffness):
    T = np.zeros([4,4])
    T[:,0] = np.array([(cos(teta))**2, sin(teta)*cos(teta),-(cos(teta))**2, -sin(teta)*cos(teta)])
    T[:,1] = np.array([sin(teta)*cos(teta), (sin(teta))**2, -sin(teta)*cos(teta), -(sin(teta))**2])
    T[:,2] = np.array([-(cos(teta))**2, -sin(teta)*cos(teta), (cos(teta))**2, sin(teta)*cos(teta)])
    T[:,3] = np.array([-sin(teta)*cos(teta), -(sin(teta))**2, sin(teta)*cos(teta), (sin(teta))**2])
    L = np.multiply(stiffness, T)
    return L

# 3.c. Membuat fungsi mat_stiff_global, yang memiliki luaran berupa matriks stiffness global setiap elemen
#      untuk input mat_stiff_lokal, node-kanan, node-kiri, dan jml node.

def mat_stiff_global (mat_stiff_lokal, p1, p2, n): 
    G = np.zeros([n,n])
    #Setiap data pada matriks stiffness lokal dicopy ke matriks stiff global pada indeks khusus
    G[2*p1-2,2*p1-2] = mat_stiff_lokal[0,0] 
    G[2*p1-1,2*p1-2] = mat_stiff_lokal[1,0]
    G[2*p1-2,2*p1-1] = mat_stiff_lokal[0,1]
    G[2*p1-1,2*p1-1] = mat_stiff_lokal[1,1]
        
    G[2*p2-2,2*p1-2] = mat_stiff_lokal[2,0]
    G[2*p2-1,2*p1-2] = mat_stiff_lokal[3,0]
    G[2*p2-1,2*p1-1] = mat_stiff_lokal[3,1]
    G[2*p2-2,2*p1-1] = mat_stiff_lokal[2,1]
        
    G[2*p1-1,2*p2-1]=mat_stiff_lokal[1,3]
    G[2*p1-2,2*p2-2]=mat_stiff_lokal[0,2]
    G[2*p1-1,2*p2-2] =mat_stiff_lokal[1,2]
    G[2*p1-2,2*p2-1] =mat_stiff_lokal[0,3]
        
    G[2*p2-1,2*p2-1] = mat_stiff_lokal[3,3]
    G[2*p2-2,2*p2-2] = mat_stiff_lokal[2,2]
    G[2*p2-1,2*p2-2] = mat_stiff_lokal[3,2]
    G[2*p2-2,2*p2-1] = mat_stiff_lokal[2,3]
    
    return G


# 3.d. Setelah fungsi mat_stiff_lokal dibuat, dibuat array L yang berisi kumpulan -
#      matriks stiffness lokal semua elemen

L = np.zeros([4, 4*jml_elemen]) # orde array L adalah 4 x 4*juml elemen 
for i in range(jml_elemen):
    # setiap empat kolom array L secara berurutan diisi matriks stiff lokal satu elemen
    L[:, 4*i: 4*(i+1)] = mat_stiff_lokal(sudut[i],stiff[i]) 
    print("\nMatriks stiffness lokal elemen ke-", str(i), "\n", L[:, 4*i: 4*(i+1)])


# 3.e. Semua matriks stiffness lokal dikonversi menjadi bentuk global, kemudian- 
#      dikumpulkan dalam matriks G

dimensi_global = 2*jml_node
G = np.zeros([dimensi_global, jml_elemen*dimensi_global])
for i in range (jml_elemen):
    G[:, 10*i : 10*(i+1)] = mat_stiff_global(L[:, 4*i : 4*(i+1)],int(nodei[i]),int(nodej[i]),dimensi_global)
    print("\nMatriks stiffness global elemen ke-", str(i),"\n", G[:, 10*i : 10*(i+1)])


# 3.f. Membuat matriks global sistem = G1 + G2 + G3+ .. + Gn

mat_global = np.zeros([dimensi_global,dimensi_global])
for i in range(jml_elemen):
    mat_global = mat_global + G[:, 10*i : 10*(i+1)]

print('\nMatriks stiffness global sistem\n', mat_global)



'''----------------------------------------------------------------------------
4. Menyelesaikan analisis 2D truss menggunakan aljabar linear untuk mendapatkan
   DISPLACEMENT
----------------------------------------------------------------------------'''

# 4.a.Satukan matriks global sistem dengan vektor gaya eksternal untuk menghasilkan -
#     augmented matrix

mat_aug_truss = np.concatenate((mat_global, force.T), axis=1)


# 4.b. Terapkan boundary condition, U1x = 0, U1y = 0, U3x= 0, U3y=0

for i in range(dimensi_global):
    mat_aug_truss[0,i] = 0
    mat_aug_truss[1,i] = 0
    mat_aug_truss[4,i] = 0
    mat_aug_truss[5,i] = 0
    
mat_aug_truss[0,0] = 1
mat_aug_truss[1,1] = 1
mat_aug_truss[4,4] = 1
mat_aug_truss[5,5] = 1 

print('\nmatriks augmented \n', mat_aug_truss)


# 4.c. Membuat Fungsi Eliminasi Gauss Jordan dengan input augmented matrix dan output solusi pers.linear

def gauss(aug_mat):  
    dimensi = len(aug_mat[:,0])

    for i in range(dimensi):
        if aug_mat[i][i] == 0.0:
            break
        
        for j in range(dimensi):
            if i != j:
                ratio = aug_mat[j][i]/aug_mat[i][i]

                for k in range(dimensi+1):
                    aug_mat[j][k] = aug_mat[j][k] - ratio * aug_mat[i][k]
    x = np.zeros([dimensi])
    for i in range(dimensi):
        x[i] = aug_mat[i][dimensi]/aug_mat[i][i]
    return (x)

displ = gauss(mat_aug_truss)
print("\nDisplacement\n",displ)

'''----------------------------------------------------------------------------
4. Menyelesaikan analisis 2D truss menggunakan aljabar linear untuk mendapatkan
   REACTION FORCE (R = KG*U - F)
----------------------------------------------------------------------------'''

R = mat_global.dot(displ) - force
print("\nReaction Force\n", R)












