## Tutorial membaca file eksternal

print(3 * "=", "Membaca File txt", 3 * "=")
file = open(r"data.txt", mode="r")

print(f"Status read : {file.readable()}")
print(f"Status read : {file.writable()}")


# print(file.read()) #baca seluruh file
print(file.readline(), end="")  # baca baris pertama
print(file.readline(), end="")  # baca baris kedua

# baca seluruh baris sebagai list
# print(file.readlines())


print(f"apakah file sudah di close: {file.closed}")
file.close()
print(f"apakah file sudah di close: {file.closed}")


##salah satu teknik membuka file di python
print("\n", 3 * "=", "Membaca file txt dengan with", 3 * "=")

with open("data.txt", mode="r") as file:
    content = file.readline()
    print(content, end="")
    print(f"apakah file sudah di close: {file.closed}")

print(f"apakah file sudah di close: {file.closed}")
