import datetime


data_waktu = datetime.datetime.now()
# cara cek library: klik kanan : go to reference
# python standard galery
print(f"datetime now {data_waktu}")
print(f"tahun : {data_waktu.year}")
print(f"tahun : {data_waktu.strftime('%A')}")

from collections import Counter  # untuk menghitung jumlah member

data = ["a", "b", "c", "b"]
data_count = Counter(data)
print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")
print(f"jumlah b = {data_count['b']}")
# count = 0
# for i in data:
#     if i == "a":
#         count += 1
# print(count)


# baca text/file
import io

file = io.open("fileText.txt", "r")
print(file.read())
