##---- LIST----

# kumpulan data numbers
data_angka = [1, 2, 3]
print(data_angka)

# kumpulan data string
data_string = ["Ucup", "Otong", "Odah"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# kumpulan campuran
data_campuran = [1, "bala-bala", 2, "cireng", "Ucup", True, "Otong", False]
print(data_campuran)

##cara alternatif membuat list
data_range = range(0, 10, 2)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehensive
list_pake_for = [i**10 for i in range(0, 10)]
print(list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0, 10) if i != 5]
print(list_pake_for_if)
# ganjil
list_pake_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_pake_for_if)
# genap
list_pake_for_if = [i for i in range(0, 10) if i % 2 != 0]
print(list_pake_for_if)
