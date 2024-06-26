class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("ini show info di class hero")
        print("{}\n\thealth: {}".format(self.name, self.health))


class Hero_intelligent(Hero):
    def __init__(self, name):
        # mengambil
        super().__init__(name, 100)

    def showInfo(self):
        # override menimpa yang ada di super class
        print("ini show info di sub class Hero_intelligent")
        print(
            "{} \n\tTipe : intelligent, \n\thealth: {}".format(self.name, self.health)
        )


class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)


lina = Hero_intelligent("lina")
axe = Hero_strength("axe")

axe.showInfo()
