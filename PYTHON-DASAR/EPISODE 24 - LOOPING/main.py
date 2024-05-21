# perulangan (Loop)

# angka = 1
# angka = angka + 1
# print(angka)
# angka = angka + 1
# print(angka)

# for kondisi:
#   aksi

# ini dengan list
print(5 * "=" + "ini dengan list" + 5 * "=")
angka2_list = [0, 2, 4, 8, 10]  # ini adalh list
print(angka2_list)

for i in angka2_list:
    print(f"i sekarang --> {i}")

print("ini adalah akhir program 1")

# ini dengan range
print("\n" + 5 * "=" + "ini dengan range" + 5 * "=")
angka2_range = range(5)

for i in angka2_range:
    print(f"i sekarang --> {i}")

print("ini adalah akhir program 2\n")

angka2_range = range(1, 5)

for i in angka2_range:
    print(f"i sekarang --> {i}")
    print("saya keren")

print("ini adalah akhir program 3\n")

# ini dengan string
print("\n" + 5 * "=" + "dengan string" + 5 * "=")

data_str = "Saya ganteng abis"

for huruf in data_str:
    print(huruf)
print("ini adalah akhir program 4\n")
