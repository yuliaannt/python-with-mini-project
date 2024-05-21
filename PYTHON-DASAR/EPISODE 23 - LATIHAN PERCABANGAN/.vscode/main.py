# latihan : kalkulator sederhana

print(20 * "=")
print("Kalkulator Sederhana")
print(20 * "=" + "\n")

angka_1 = float(input("Masukkan angka 1 = "))
operator = input("Operator (+,-,x,/) = ")
angka_2 = float(input("Masukkan angka 2 = "))

# percabangan
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "*" or operator == "x":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else:
    print("Masukkan yang bener dong, aku pusing")

print("Ini adalah akhir program")
