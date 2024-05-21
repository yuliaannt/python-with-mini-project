# operator dalam bentuk method

3  # merubah case dari string

# merubah semua ke upper case
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke upper case
alay = " aKu KeCe AbieezZzZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

##pengecekan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower()
print(salam + " is lower =" + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isnum() <-- huruf dan angka
# iddecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle <-- semua kata dimulau dengan huruf besar

judul = "Its is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + "is title = " + str(cek_judul))

## cek komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppa")
print("end = " + str(cek_end))

##penggabungan komponen join() split()
pisah = ["aku", "sayang", "kamu"]
gabungan = ",".join(pisah)
print(pisah)

# cara copy shift alt
gabungan = " ".join(pisah)
print(gabungan)

gabungan = "ehm".join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split("ehm"))

##Alokasi karakter rjust(), ljust(), , center()
print(5 * "=" + "data" + "=" * 5)

kanan = "surotong".rjust(10)
print("'" + kanan + "'")

kiri = "surotong".ljust(10)
print("'" + kiri + "'")

tengah = "surotong".center(10)
print("'" + tengah + "'")

tengah = "surotong".center(20, ":")
print("'" + tengah + "'")

# kebalikannya --> strip
tengah = tengah.strip(":")
print("'" + tengah + "'")

kanan = kanan.strip()
print("'" + kanan + "'")
