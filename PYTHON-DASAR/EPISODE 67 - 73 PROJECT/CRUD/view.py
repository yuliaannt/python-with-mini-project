from . import operasi


def update_console():
    read_console()
    while True:
        print("pilih nomer buku yang akan di update")
        no_buku = int(input("Nomor Buku : "))
        data_buku = operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("nomor tidak valid silahkan masukkan lagi")

    data_break = data_buku.split(",")
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while True:
        # data yang ingin di update
        print("\n" + "=" * 100)
        print("silahkan pilih data anda yang akan anda ubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # memilih mode untuk di update
        user_option = input("Pilih data [1,2,3]: ")
        print("\n" + "=" * 100)
        match user_option:
            case "1":
                judul = input("judul\t: ")
            case "2":
                penulis = input("penulis\t: ")
            case "3":
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
                        print(
                            "Tahun harus angka, silahkan masukan kembali dengan format (yyyy)"
                        )
            case _:
                print("index tidak cocok bang")

        print("Data baru anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        is_done = input("Apakah selesai update (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break
    operasi.update(no_buku, pk, data_add, tahun, judul, penulis)


def create_console():
    print("\n\n" + "=" * 100)
    print("Silahkan tambah data buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
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

    operasi.create(tahun, judul, penulis)
    print("\nBerikut adalah data baru anda")

    read_console()


def read_console():
    data_file = operasi.read()
    index = "No"
    penulis = "Penulis"
    judul = "Judul"
    tahun = "Tahun"

    # header
    print("\n" + "=" * 100)
    print(f"{index:4} | {penulis:40} |{judul:40} | {tahun:5}")
    print("-" * 100)

    # data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {penulis:.40} | {judul:.40} | {tahun:4}", end="")

    # footer
    print("=" * 100 + "\n")
