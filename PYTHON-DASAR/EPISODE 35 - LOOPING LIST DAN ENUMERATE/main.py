# looping dari list

# for loop
kumpulan_angka = [4, 3, 2, 4, 5, 6]

for angka in kumpulan_angka:
    print(f"angka = {angka}")
peserta = ["ucup", "otong", "dadang", "diding"]

for nama in peserta:
    print(f"nama = {nama}")

    # for loop  dan range
    # mengambil indeks tertentu
print("\n for loop")
kumpulan_angka = [1, 2, 3, 4, 5, 6, 7]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka}")

# while loop
print("\n while loop")
kumpulan_angka = [1, 2, 3, 4, 5, 6, 7]

panjang = len(kumpulan_angka)
while i < panjang:
    print(f"angka = {kumpulan_angka}")
    i += 1

# list comperhension
print("\n List Comprehension")

data = ["Ucup", 1, 2, 3, "otong"]
[print(f"data = {i}") for i in data]

angka = [1, 2, 3, 4, 5, 6, 7]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("\n Enumerate")

data_list = ["Ucup", 1, 2, 3, "otong"]

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
