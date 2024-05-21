# continue, pass, break

# pass -> dia berfungsi sebagain dummy, tidak akan dieksekusi

# angka = 0

# while angka < 5:
#     angka += 1
#     if angka == 3:
#         pass  # tidak akan dieksekusi
#     print(angka)

# continue
angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang adalah {angka}")  # aksi 1

    if angka == 3:
        print("nice!")
        continue  # akan membuat loop loncat ke aksi selanjutnyq

    print("whatsapp")  # aksi 2

print("Finish")
