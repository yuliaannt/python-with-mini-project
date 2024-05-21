data_0 = [1, 2]
data_1 = [3, 4]

data_2D = [data_0, data_1, 10]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
# mengambil

data = data_2D[0][1]
print(f"data = {data}")

print(f"Address asli = {hex(id(data_2D))}")
print(f"Address copy = {hex(id(data_2D_copy))}")

print(f"Adress dari member ke-1")
print(f"Address asli = {hex(id(data_2D[0]))}")
print(f"Address copy = {hex(id(data_2D_copy[0]))}")

data_2D[1][0] = 5
data_2D[2] = 9
print(f"data = {data_2D}")
print(f"data copy= {data_2D_copy}")


# kita gunakan deep copy
from copy import deepcopy

data_2D = [data_0, data_1, 10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"Address asli = {hex(id(data_2D))}")
print(f"Address ini deep = {hex(id(data_2D_deepcopy))}")
print(f"Adress dari member ke-1")
print(f"Address asli = {hex(id(data_2D[0]))}")
print(f"Address copy = {hex(id(data_2D_deepcopy[0]))}")
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep copy = {data_2D_deepcopy}")
