# break

data_int = int(input("Hitung sampai = "))
angka = 0

# while angka < 5:
#     angka += 1
#     print(f"count = {angka}")
#     # print(f" angka sekarang adalah = {angka}")

#     if angka == 3:
#         print("nice")
#         break  # melakukan stop loop di nomer 3 berbeda dengan continue yang akan loncat
#     print("wassap")

# print("Akhir")

while True:
    angka += 1
    print(f"count = {angka}")
    # print(f" angka sekarang adalah = {angka}")

    if angka == data_int:
        print("nice")
        break  # melakukan stop loop di nomer 3 berbeda dengan continue yang akan loncat
    print("wassap")

print("Akhir")
