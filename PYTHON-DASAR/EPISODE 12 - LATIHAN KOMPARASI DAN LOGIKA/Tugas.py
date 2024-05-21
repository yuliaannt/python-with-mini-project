#1. ---0++++5---8++++11----

print("=====Soal 1=====")
inputUser = float(input("Masukkan angka : "))
isLebihDari1 = inputUser > 0
print("Input lebih dari 0 : ", isLebihDari1)
isKurangDari2 = inputUser < 5
print("Input kurang dari 5 : ", isKurangDari2)
isCorrect1 = isLebihDari1 and isKurangDari2

isLebihDari3 = inputUser > 8
print("Input kurang dari 8 : ", isLebihDari1)
isKurangDari4 = inputUser < 11
print("Input lebih dari 11 : ", isKurangDari2)
isCorrect2 = isLebihDari1 and isKurangDari2

hasil = isCorrect1 or isCorrect2
print ("Hasil dari soal 1 adalah ", hasil)

print("\n",10*"=","\n")


#2. ++++0---5++++8---11++++
print("=====Soal 2=====")
inputUser = float(input("Masukkan angka : "))
isKurangDari1 = inputUser < 0
print("Input kurang dari 0 : ", isKurangDari2)
isLebihDari1 = inputUser > 5
print("Input lebih dari 5 : ", isLebihDari1)
isCorrect3 = isLebihDari1 and isKurangDari2


isKurangDari3 = inputUser < 8
print("Input kurang dari 8 : ", isKurangDari3)
isLebihDari4 = inputUser > 11
print("Input lebih dari 11 : ", isLebihDari4)
isCorrect4 = isLebihDari1 and isKurangDari2

hasil = isCorrect3 or isCorrect4
print ("Hasil dari soal 2 adalah ", hasil)