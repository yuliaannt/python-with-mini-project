# Lamda function


def f_kuadrat(angka):
    return angka**2


print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

# kita coba dengan lambda
# output = lamda argument: expression
kuadrat = lambda angka: angka**2
print(f"hasil lamda kuadrat = {kuadrat(5)}")

# dua input
pangkat = lambda num, pow: num**pow
print(f"hasil lamda pangkat ={pangkat(2,3)}")

## kegunaan
# sorting untuk list biasa
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort()
print(f"sorted list = {data_list}")


# sorting dia pakai panjang
def panjang_nama(nama):
    return len(nama)


data_list.sort(key=len)
print(f"sorted list by panjang = {data_list}")

# sort pakai lambda
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort(key=lambda nama: len(nama))
print(f"sorted list by lambda = {data_list}")

# filter
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def kurang_dari_lima(angka):
    return angka < 5


data_angka_baru = list(filter(kurang_dari_lima, data_angka))
data_angka_baru = list(filter(lambda x: x < 7, data_angka))
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x: (x % 2 == 0), data_angka))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x: (x % 2 != 0), data_angka))
print(data_ganjil)

# kelipatan 3
data_3 = list(filter(lambda x: (x % 3 == 0), data_angka))
print(data_3)


# anonymous func
# currying <- Haskell curry


def pangkat(angka, n):
    hasil = angka**n
    return hasil


data_hasil = pangkat(5, 2)
print(f"fungsi biasa = {data_hasil}")


# currying
def pangkat(n):
    return lambda angka: angka**n


pangkat2 = pangkat(2)
print(f"pangkat2 = {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"pangkat2 = {pangkat3(3)}")
print(f"pangkat bebas= {pangkat(4)(5)}")
