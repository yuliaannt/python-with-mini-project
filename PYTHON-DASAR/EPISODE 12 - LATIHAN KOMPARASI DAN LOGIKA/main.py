# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++++3---------10+++++
print("====Kasus Satu===")
inputUser = float(
    input("Masukkan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10: ")
)

print("====Kasus Satu===")
# ++++++3-----------
# memeriksa angka kurang dari 3
isKurangDari = inputUser < 3
print("Kurang dari 3 :", isKurangDari)

# ---------10+++++
# memeriksa angka lebih dari 10
isLebihDari = inputUser > 10
print("Lebih dari 10: ", isLebihDari)

# ++++++3---------10+++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan : ", isCorrect)


print("\n", 10 * "=", "\n2")
print("====Kasus Dua====")
# ----3+++++++10---- irisan
inputUser = float(
    input("Masukkan angka yang bernilai \nlebih dari 3 \ndan \nkurang dari 10: ")
)
# ----3++++
isLebihDari = inputUser > 3
print("Lebih dari 3 : ", isLebihDari)
# ++++10----
isKurangDari = inputUser < 10
print("Kurang dari 10 : ", isKurangDari)

isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukkan : ", isCorrect)
