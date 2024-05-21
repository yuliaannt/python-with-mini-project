"""Fungsi dengan argument (input)"""


# '''
# def nama_fungsi(argument):
#   badan fungsi
# '''
def hello_world(nama):
    """fungsi hello world menerima input dengan variabel nama"""
    print(f"selamat datang di dunia wahai {nama}")


hello_world("ucup")


def tambah(angka_1, angka_2):
    """Fungsi tambah"""
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")


tambah(2, 3)
tambah(10000, 1)


def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")


anggota_boyband = ["ucup", "otong", "dudung"]

say_hi(anggota_boyband)

print(anggota_boyband[1])
