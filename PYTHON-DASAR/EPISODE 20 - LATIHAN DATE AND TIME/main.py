# Date and time (Latihan)

import datetime as dt

hari_ini = dt.date.today()

print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}")

tanggal = dt.date(2005, 10, 10)
print(tanggal)
print(f"Hari ini adalah hari = {tanggal:%A}")

print("Silahkan masukan tanggal, \nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal\t:"))
bulan = int(input("Bulan\t :"))
tahun = int(input("Tahun\t :"))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal:  {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Harinya adalah = {tanggal_lahir:%A}")
print(f"umur anda adalah : {umur_hari}")
print(f"umur anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan")
