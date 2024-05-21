class Mangga:

    # magic method
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    # digunakan dalam debug
    def __repr__(self) -> str:
        return "Debug: Mangga: {} dengan jumlah {}".format(self.nama, self.jumlah)

    # dipakai jika program sudah jadi
    def __str__(self) -> str:
        return "Debug: Mangga: {} dengan jumlah {}".format(self.nama, self.jumlah)

    def __add__(self, objek):
        return self.jumlah + objek.jumlah

    @property
    def __dict__(self):
        return "objek ini mempunyai nama dan jumlah"


belanja1 = Mangga("armanis", 10)
belanja2 = Mangga("mana lagi", 5)
print(repr(belanja1))
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)
