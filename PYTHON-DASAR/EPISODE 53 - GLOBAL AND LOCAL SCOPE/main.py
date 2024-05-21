##GLOBAL DAN LOCAL SCOPE

nama_global = "otong"  # <-- variabel global dimana dapat diakses didalam fungsi


# akses variabel global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {nama_global}")


fungsi()

# akses variabel global dalam loop
for i in range(0, 5):
    print(f"loop {i} - {nama_global}")

# percabangan
if True:
    print(f"if menampilkan {nama_global}")


##variabel local scope
def fungsi2():
    nama_local = "Ucup"  # variabel local scope


# fungsi2()
# # print(nama_local) #tidak dapat diakses


# contoh 1 : penggunaan akses variabel
# nama = "otong" #bisa diletakkan setelah panggil say_otong()
def say_otong():
    print(f"Hello {nama}")


nama = "otong"
say_otong()

# contoh 2 : merubah variabel global
angka = 0
nama = "ucup"


def ubah_angka(nilai_baru, nama_baru):
    global angka
    global nama
    angka = nilai_baru
    nama = nama_baru


print(f"sebelum {angka, nama}")
ubah_angka(10, "Tita")
print(f"sesudah {angka,nama}")

for i in range(0, 5):
    angka += i
    angka_dummy = 0
print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)
