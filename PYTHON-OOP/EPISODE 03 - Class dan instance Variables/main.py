# template
class Hero:
    # variabel static (class variabel)
    jumlah = 0  # nempel pada class

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # intance variabel
        self.name = inputName  # nempel bada object
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("membuat hero dengan nama: " + inputName)


# object
hero1 = Hero("sniper", 100, 10, 4)
print(hero1.jumlah)
hero2 = Hero("mirana", 100, 3, 4)
print(hero2.jumlah)

print(Hero.__dict__)  # atribut hero tidak ada : variabel static
