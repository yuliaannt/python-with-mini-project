import datetime

mahasiswa1 = {
    "nama": "si ucup surucup",
    "NIM": "26528592",  # jangan pakai int
    "SKS_lulus": 130,
    "beasiswa": False,
    "lahir": datetime.datetime(2003, 4, 10),
}

mahasiswa2 = {
    "nama": "Otong surotong",
    "NIM": "26528593",  # jangan pakai int
    "SKS_lulus": 140,
    "beasiswa": True,
    "lahir": datetime.datetime(2004, 9, 30),
}
mahasiswa3 = {
    "nama": "Asep",
    "NIM": "26528594",  # jangan pakai int
    "SKS_lulus": 150,
    "beasiswa": False,
    "lahir": datetime.datetime(2004, 9, 20),
}

data_mahasiswa = {
    "MAH001": mahasiswa1,
    "MAH002": mahasiswa2,
    "MAH003": mahasiswa3,
}

# print(data_mahasiswa)
print(f"{'key':<6} {'Nama':<17} {'SKS':<9} {'Beasiswa':<9} {'Lahir':<10}")
print("-" * 50)

for mahasiswa in data_mahasiswa:
    key = mahasiswa

    Nama = data_mahasiswa[key]["nama"]
    NIM = data_mahasiswa[key]["NIM"]
    SKS = data_mahasiswa[key]["SKS_lulus"]
    BEASISWA = data_mahasiswa[key]["beasiswa"]
    LAHIR = data_mahasiswa[key]["lahir"].strftime("%x")
    print(f"{key:<6} {Nama:<17} {SKS:<9} {BEASISWA:<9} {LAHIR:<10}")


# <6 rata kiri, >6 rata kanan, ^center
