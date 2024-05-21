class Hero:
    # class variabl
    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # varaibel instance private
        self.__private = "private"
        # variabel instance protected
        self._protected = "protected"  # sama seperti public tapi tidak boleh di rubah


lina = Hero("Lina", 100)

print(lina.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah)
# print(lina._protected)
# lina.__private = "testing"
# # lina.name=10
# print(lina.health)
# print(lina.__dict__)

# lina._protected = "testing"
# print(lina.__dict__)
# print(lina._protected)
