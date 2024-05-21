# exception akan terjadi saat program mengalami error saat run time

# contoh sederhana untuk menangkap exception
# from math import nan

# input_user = int(input("masukkan angka: "))
# hasil = nan

# try:
#     hasil = 10 / input_user
# except:
#     print("input tidak boleh 0")

# print(f"hasil = {hasil}")


while True:
    angka = int(input("masukkan angka pembagi : "))
    try:
        hasil = 10 / angka
        print(f"hasil = {hasil}")
        is_done = input("lanjutkan (y/n)? ")
        if is_done == "n":
            break

    except:
        print("pembagi nol, silahkan masukkan input lagi")
print("ini akhir dari program-1")


# while True:
try:
    with open("data.txt", "r") as file:
        print(file.read())
except:
    with open("data.txt", "w", encoding="utf-8") as file:
        print("data.txt tidak ditemukkan, membuat file baru")
        file.write("file baru")
        # break
print("ini akhir dari program-2")
