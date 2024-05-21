# studi kasus pip
import numpy as np  # digunakan untuk matriks

list_a = [1, 2, 3, 4, 5]
vector_a = np.array([1, 2, 3, 4])

print(f"ini list_a = {list_a}")
print(f"ini vector_a = {vector_a}")
# perbedaan
# kalo di kuadratin/pangkat 1. List tidak bisa 2. array bisa
# print(list_a**2)
# print(vector_a * 2)

matrix_b = np.array([(1, 2), (3, 2)])
print(f"ini adalah \n{matrix_b**2}")

zeros_c = np.zeros((2, 2))
print(f"zeros c = \n{zeros_c}")

ones_d = np.ones((2, 2))
print(f"ones d = \n{ones_d}")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah {jumlah}")
