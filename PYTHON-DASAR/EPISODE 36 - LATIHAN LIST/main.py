# membuat database sederhana

list_buku = []
# program list buku
while True:
    print(5 * "=" + "Masukkan judul buku" + 5 * "=")
    judul = input("masukkan judul buku\t : ")
    penulis = input("penulis\t: ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("=" * 10)
    print("No.| Judul| Penulis")
    for index, buku in enumerate(list_buku):
        print(f"{index} | {buku[0]}| {buku[1]}")
    # print(list_buku)

    print("=" * 10)
    isLanjut = input("Apakah dilanjutkan? (y/n)")

    if isLanjut == "n":
        break
print("PROGRAM SELESAI")
