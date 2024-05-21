# modul matematika dengan import
from matematika import tambah as tb
from matematika import kali as kl
from matematika import pangkat as pg

import matematika as math

# from matematika import *

hasil_tambah = tb(1, 2, 3, 4, 5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = math.kl(1, 2, 3, 4, 5)
print(f"hasil kali = {hasil_kali}")

hasil_pangkat = pg(1, 2, 3, 4, 5)
print(f"hasil pangkat = {hasil_pangkat}")
