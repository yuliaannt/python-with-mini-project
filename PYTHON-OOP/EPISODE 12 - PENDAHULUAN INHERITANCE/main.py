class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health


class Hero_intelligent(Hero):
    pass


class Hero_strength(Hero):
    pass


lina = Hero("lina", 100)
techies = Hero_intelligent("techis", 50)
Hero_strengt = Hero_strength("axe", 20)

print(lina.name)
print(techies.name)
print(techies.name)
