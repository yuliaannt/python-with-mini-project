data_angka = [1, 3, 4, 5, 6, 3, 4, 5, 6, 2, 4, 7, 5, 3]
print(f"Ini adalah data angka = \n{data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)

data = ["Ucup", "Otong", "Dudung", "Ujang"]
index_dudung = data.index("Dudung")
index_ujang = data.index("Ujang")
print(f"index si Dudung = {index_dudung}")
print(f"index si Ujang = {index_ujang}")

# mengurutkan list
print(f"Data angka sebelum sort = {data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = \n{data}")
data.sort()
print(f"data sort = \n{data}")

# balik list
data_angka.reverse()
data.reverse()
print(f"data angka reverse = \n{data_angka}")
print(f"data reverse= \n{data}")
