## Teknik menduplikat list

a = ["Ucup", "Otong", "Dudung"]
print(f"a = {a}")

b = a  # pass by refence
print(f"b ={b}")

# kita akan merubah member dari a
# ini akan merubah kedua list
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b ={b}")

# address dari kedua list
print(f"address a = {hex(id(a))}")
print(f"address a = {hex(id(b))}")

# menduplikat list dengan copy

print(5 * "=" + "Membubuat list c dengan a.copy()" + "=" * 5)
c = a.copy()  # full duplicate / data baru
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(5 * "=" + "Mengubah data 0" + "=" * 5)
c[0] = "Dadang"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(5 * "=" + "Mengubah data 1" + "=" * 5)
a[1] = "Otong"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
