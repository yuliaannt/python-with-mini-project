import sains
from sains.matematika import scientific

hasil_tambah = sains.matematika.tambah(1, 2, 3, 4, 5)
print(f"hasil tambah = {hasil_tambah}")

hasil_fisika = sains.fisika.gaya(1, 5)
print(f"hasil fisika = {hasil_fisika}")

hasil_kali = sains.matematika.kali(1, 5)
print(f"hasil kali = {hasil_kali}")

pangkat3 = scientific.pangkat(5)
print(f"hasil pangkat 3 = {pangkat3(5)}")

# from sains import *

# hasil_tambah = matematika.basic.tambah(1, 2, 3, 4, 5)
# print(f"hasil tambah = {hasil_tambah}")

# hasil_fisika = fisika.gaya(1, 5)
# print(f"hasil fisika = {hasil_fisika}")

# hasil_kali = matematika.basic.kali(1, 2, 3, 4)
# print(f"hasil kali = {hasil_kali}")
