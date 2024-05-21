# Latihan perulangan membuat segitiga

sisi = 10

# 1. menggunakan for
# dummy variable
count = 1
for i in range(sisi):
    print("*" * count)
    count += 1
print("Akhir For\n")

# 2. menggunkan while

count = 1
while True:
    print("*" * count)
    count += 1

    if count > sisi:
        break
print("Akhir While\n")


# 3. hanya ganjil saja
count = 1
while True:
    if count % 2:
        # print jika ganjil
        print("*" * count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break
print("Akhir segitiga siku \n")

# 4. hanya ganjil saja
count = 1
spasi = int(sisi / 2)
while True:
    if count % 2:
        # print jika ganjil
        print(" " * spasi, "+" * count)
        spasi -= 1
        count += 1
    else:  # jika bukan ganjil, maka periksa ulang ke if hingga > sisi(break)
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break
print("Akhir segitiga sama sisi\n")

print(5 * "=" + "Tugas: keupat" + "=" * 5)
for i in range(0, 5):
    print(" " * (5 - i), end="")
    for x in range(i):
        print("+ ", end="")

    print()
for i in range(5, 0, -1):
    print(" " * (5 - i), end="")
    for x in range(i):
        print("+ ", end="")
    print()
