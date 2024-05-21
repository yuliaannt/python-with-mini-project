from . import database
from .util import random_string
from time import time
import time


def update(no_buku, pk, data_add, tahun, judul, penulis):
    data = database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul) :]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]}, {data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    panjang_data = len(data_str)

    try:
        with open(database.DB_NAME, "r+", encoding="utf-8") as file:
            file.seek(panjang_data * (no_buku - 1))
            file.write(data_str)
    except:
        print("error dalam update")


def create(tahun, judul, penulis):
    data = database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul) :]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]}, {data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        with open(database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit ditambahkan boss, gagal maning")


def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print(
                    "Tahun harus 4 digit, silahkan masukan kembali dengan format (yyyy)"
                )
        except:
            print("Tahun harus angka, silahkan masukan kembali dengan format (yyyy)")

    data = database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul) :]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]}, {data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)
    try:
        with open(database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udalah gagal boss")


def read(**kwargs):
    try:
        with open(database.DB_NAME, "r") as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"] - 1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("membaca database error")
        return False
