# import time

# t_start = time.time()

from sains import fisika
import sains.matematika
from sains.fisika import gaya as gy

hasil_tambah = sains.matematika.tambah(1, 2, 3, 4, 5)
print(f"hasil tambah dari package adalah {hasil_tambah}")
# t_end = time.time()

gaya = fisika.gaya(90, 10)
print(f"gaya = {gaya}")

gaya = gy(90, 10)
print(f"gaya = {gaya}")
