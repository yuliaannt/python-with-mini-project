# Operasi

# index   0      1(-2)     2(-1)
data = ["ucup", "otong", "Dudung"]

# mengambil data dari list ini
data_0 = data[0]
print(f"Data pertama(index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"ini adalah panjang data = {panjang_data} ")


## manipulasi data lis
# menambahkan item pada list sesuai posisi
print(f" Data sebelum ditambah = {data}")
# data.insert(posisi, item)
data.insert(1, "Asep")
print(f"Data setelah ditambah = \n{data}")

# menambah di akhir list
data.append("Jajang")
print(f"Data setelah ditambah = \n{data}")

# menambah list dengan list
data_baru = ["Ujang", "Usep", "Dadang"]
data.extend(data_baru)
print(f"Data gabungan = \n{data}")


# merubah data
# kita ubah data 2 menjadi michle
data[2] = "michle"
print(f"Data rubah = \n{data}")

# remove data
data.remove("Ujang")  # harus sesuai huruf
print(f"Data remove = \n{data}")

# remove data paling belakng
data_akhir = data.pop()
print(f"Data akhir = \n{data}")

print(data_akhir)
