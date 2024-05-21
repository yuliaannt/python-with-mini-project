# format string

# contoh generic

# string
nama = "Ucup"
# str = "hello " + nama

# print(str)


format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)


# angka
angka = 2005.5
format_str = "angka = " + str(angka)
print(format_str)

angka = 2004.4
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"  # d untuk bilangan bulat
print(format_str)

# bilangan ribuan
angka = 2000
format_str = f"ribuan = {angka:,}"
print(format_str)

angka = 20000000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilagan decimal
angka = 2004.4800
format_str = f"decimal = {angka:.2f}"  # f <-- float
print(format_str)

# menampilkan leading zero
angka = 2004.4800
format_str = f"decimal = {angka:010.3f}"  # 8 = total, f <-- float
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f"angka minus = {angka_minus:+d}"
format_plus = f"angka plus = {angka_plus:.2f}"

print(format_minus)
print(format_plus)


# memformat persen
persentase = 0.076
format_persen = f"persen = {persentase:.2%}"

print(format_persen)

# melakukan operasi aritmatika di dalam place holder

harga = 1000
jumlah = 5

format_string = f"harga total = Rp{harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"Octal = {oct(angka)}"
format_hex = f"Hexa = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)
