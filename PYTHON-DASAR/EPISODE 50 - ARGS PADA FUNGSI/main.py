"""*args"""


def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi("ucup", 170, 40)


def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi(["otong", 100, 120])


# kenalan dengan args
def fungsi_args(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi_args("dudung", 120, 40)


# studi kasus
def tambah(*data):
    # data tipenya tuple
    output = 0
    for angka in data:
        output += angka
    return output


hasil = tambah(1, 2, 3, 4, 5, 6, 7)
print(f"hasil= {hasil}")

hasil = tambah(10, 5, 15)
print(f"hasil= {hasil}")
