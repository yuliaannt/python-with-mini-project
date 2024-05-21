from . import operasi

# from signal import pause

DB_NAME = "data.txt"

TEMPLATE = {
    "pk": "XXXXXX",
    "date_add": "yyyy-mm-dd",
    "penulis": 255 * " ",
    "judul": 255 * " ",
    "tahun": "yyyy",
}


def init_console():
    try:
        with open("data.txt", "r") as file:
            print("database tersedia, init done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        operasi.create_first_data()
