"""Latihan fungsi"""

import os

# os.system = "cls"
# # program menghitung luas dan keliling persegi panjang

# # membuat header
# print(f"{'MENGHITUNG LUAS PERSEGI PANJANG':^40}")
# print(f"{'MENGHITUNG KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # megambil input user
# LEBAR = int(input("Masukkan lebar: "))
# PANJANG = int(input("Masukkan panjang: "))

# # program menghitung luas
# LUAS = PANJANG * LEBAR
# KELILING = 2 * (PANJANG + LEBAR)

# # tampilkan hasilnya
# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")


def header():
    """fungsi header"""
    os.system("cls")
    print(f"{'MENGHITUNG LUAS PERSEGI PANJANG':^40}")
    print(f"{'MENGHITUNG KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")


def input_user():
    LEBAR = int(input("Masukkan lebar: "))
    PANJANG = int(input("Masukkan panjang: "))

    return LEBAR, PANJANG


def hitung_luas(LEBAR, PANJANG):
    """Fungsi Luas"""
    return LEBAR * PANJANG


def hitung_keliling(LEBAR, PANJANG):
    return 2 * (LEBAR + PANJANG)


def display(message, value):
    print(f"hasil perhitungan {message} = {value}")


while True:
    header()

    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)

    display("luas", LUAS)
    display("keliling", KELILING)
    isContinue = input("Apakah lanjut (y/n)? ")
    if isContinue == "n":
        break
print("Ini adalah akhir program")

# header maish tampil
