import numpy as np
from math import*

'''-------------------------------------------------
1. User memasukkan data elemen pada sistem truss'''

N = int(input("Banyak elemen pada sistem truss? "))
M = int(input("Banyak node pada sistem truss?"))
print("Masukkan data-data truss secara berurutan dari elemen 1 dipisah spasi")

stiff = np.array([input("Data stiffness, k : ").split(' ')], float)
nodei = np.array([input("Data node-i       : ").split(' ')], float)
nodej = np.array([input("Data node-j       : ").split(' ')], float)
sudut = np.array([input("Data sudut        : ").split(' ')], float)

'''User menginput matriks gaya eksternal pada node-node truss'''

print("\n \nMasukkan matrriks gaya eksternal (dipisah spasi)")
force = np.array([input().split(' ')], float)

'''User menginput boundary conditions'''
print("Boundary condition (Isi 0 jika node tidak bergerak, dan - jika tidak ada boundary cond)")
u = np.zeros(2*M)
for i in range(2*M):
    if i % 2 == 0:
        u[i] = float (input("Ux-", str(int(i/2 + 1))))
    else:
        u[i] = float (input("Uy-", str(int((i+1)/2))))
    

'''-------------------------------------------------
3. Buat Fungsi matriks stiffness Lokal '''
def mat_stiff_lokal (teta, stiff):
    T = np.zeros([4,4])
    T[:,0] = np.array([(cos(teta))**2, sin(teta)*cos(teta),-(cos(teta))**2, -sin(teta)*cos(teta)])
    T[:,1] = np.array([sin(teta)*cos(teta), (sin(teta))**2, -sin(teta)*cos(teta), -(sin(teta))**2])
    T[:,2] = np.array([-(cos(teta))**2, -sin(teta)*cos(teta), (cos(teta))**2, sin(teta)*cos(teta)])
    T[:,3] = np.array([-sin(teta)*cos(teta), -(sin(teta))**2, sin(teta)*cos(teta), (sin(teta))**2])
    L = np.multiply(stiff, T)
    return L

'''--------------------------------------------------------
4. Buat Fungsi matriks stiffnes Global'''

def mat_stiff_global (mat_stiff_lokal, p1, p2, n):
    G = np.zeros([n,n])
    
    G[2*p1-2,2*p1-2] = mat_stiff_lokal[0,0]
    G[2*p1-1,2*p1-2] = mat_stiff_lokal[1,0]
    G[2*p1-2,2*p1-1] = mat_stiff_lokal[0,1]
    G[2*p1-1,2*p1-1] = mat_stiff_lokal[1,1]
        
    G[2*p2-2,2*p1-1] = mat_stiff_lokal[2,0]
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

'''-----------------------------------------------------------
5. Buat Matriks Stiffness Lokal'''
L = np.zeros([4, 4*N])
for i in range(N):
    L[:, 0 : 4*(i+1)] = mat_stiff_lokal(sudut[i],stiff[i])
print('matriks stiffness lokal \n', L)


'''-----------------------------------------------------------
Buat Matriks Stiffness Global per elemen'''

dimensi_global = int(np.max(nodej))

G = np.zeros([2*dimensi_global, N*2*dimensi_global])
for i in range (N):
    G[:, 0 : 4*(i+1)] = mat_stiff_global(L[:, 0 : 4*(i+1)],int(nodei[i]),int(nodej[i]),2*dimensi_global)
    
print('matriks stiffness global per elemen\n', G)


'''------------------------------------------------------------
Buat matriks stiffness global sistem'''

mat_global = np.zeros([2*dimensi_global,2*dimensi_global])
for i in range(dimensi_global):
    mat_global = mat_global + G[i]
print(mat_global)

aug_mat_sis = np.concatenate((mat_global, force.T), axis=1)
print('mat_aug_sis \n', aug_mat_sis)

'''--------------------------------------------------------------
Boundary Condition'''


'''-------------------------------------------------------------
6. Fungsi Eliminasi Gauss Jordan'''

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

'''-------------------------------------------------------------
Selesaikan'''

displ = gauss(aug_mat_sis)

print(displ)

    
    










