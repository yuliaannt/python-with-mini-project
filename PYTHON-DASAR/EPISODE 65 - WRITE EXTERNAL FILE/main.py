# 1. mode write

# dia akan membuat file baru jika tidak ada,
# lalu akan menimpa atau overwrite isisnya

with open(f"data_1.txt", "w", encoding="utf-8") as file:
    file.write("jon si joni")

with open(f"data_1.txt", "w", encoding="utf-8") as file:
    file.write("ucup surucup")  # ketimpa overwrite

# 2. mode append, data nambah terus bila di run
with open(f"data_2.txt", "w", encoding="utf-8") as file:
    file.write("jon si joni\n")
with open(f"data_2.txt", "a", encoding="utf-8") as file:
    file.write("ucup surucup\n")
with open(f"data_2.txt", "a", encoding="utf-8") as file:
    file.write("Tambah lagi dengan append")

# # 3. mode r+
with open("data_3.txt", "w", encoding="utf-8") as file:
    file.write("data ke 3\n")

with open(f"data_3.txt", "r+", encoding="utf-8") as file:
    file.write("baris-1 \n")  # data_1 'w' ketimpa
    # data = file.read()
    # print(data)
    file.write("baris-2 \n")
    file.write("baris-3 \n")

with open("data_3.txt", "r+", encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt", "r+", encoding="utf-8") as file:
    file.write("otong")  # menimpa isi text sesuai panjang data
