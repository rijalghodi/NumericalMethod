import numpy as np
temp = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]

# Mendefinisikan variabel suhu_lama berisi suhu node 1
# pada perhitungan sebelumnya
suhu_lama = temp[1]
# Membuat Augmented matriks
aug_mat = np.zeros((10,11))
for i in range (10):
    if i == 0:
        aug_mat[0,0] = -3
        aug_mat[0,1] = 1
        aug_mat[0,10] = -530
    elif i == 9:
        aug_mat[9,8] = 1
        aug_mat[9,9] = -4
        aug_mat[9,10] = -90
    else:
        aug_mat[i,i-1] = 1
        aug_mat[i,i] = -3
        aug_mat[i , i+1] = 1
        aug_mat[i,10] = -30
# Menyelesaikan Augmented matriks memakai eliminasi Gauss-Jordan
for i in range(10):
    for j in range(10):
        if i != j:
            ratio = aug_mat[j][i]/aug_mat[i][i]
            for k in range(11):
                aug_mat[j][k] = aug_mat[j][k] - ratio * aug_mat[i][k]
for i in range(10):
    temp[i] = round(aug_mat[i,10]/aug_mat[i,i],2)
print(temp)