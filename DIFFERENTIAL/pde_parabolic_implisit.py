"""KONDUKSI TRANSIEN METODE IMPLISIT"""
import numpy as np

temp = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
delta = 1;
p = 0
while delta > 0.1:
	# Menampilkan sebaran temperatur setiap 0.1 sekon
	print("t = ", str(p * 0.1))
	print(temp)
	# Mendefinisikan variabel suhu_lama berisi suhu node 1
	# pada perhitungan sebelumnya
	suhu_lama = temp[1]
	# Membuat Augmented matriks
	aug_mat = np.zeros((10, 11))
	for i in range(10):
		aug_mat[i, i] = 1.15
		if i == 0:
			aug_mat[0, 1] = -0.05
			aug_mat[0, 10] = temp[0] + 26.5
		elif i == 9:
			aug_mat[9, 8] = -0.05
			aug_mat[9, 10] = temp[9] + 4.5
		else:
			aug_mat[i, i - 1] = -0.05
			aug_mat[i, i + 1] = -0.05
			aug_mat[i, 10] = temp[i] + 1.5
	# Menyelesaikan Augmented matriks memakai eliminasi Gauss-Jordan
	for i in range(10):
		for j in range(10):
			if i != j:
				ratio = aug_mat[j][i] / aug_mat[i][i]
				for k in range(11):
					aug_mat[j][k] = aug_mat[j][k] - ratio * aug_mat[i][k]
	for i in range(10):
		temp[i] = round(aug_mat[i, 10] / aug_mat[i, i], 2)

	# Mendefinisikan delta sebagai selisih suhu noda 1 yang lama dan baru
	delta = abs(suhu_lama - temp[1])
	p = p + 1
