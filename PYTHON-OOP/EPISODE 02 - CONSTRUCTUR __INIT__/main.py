# template
class Hero:
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("sniper", 100, 10, 4)
hero2 = Hero("mirana", 100, 3, 4)
print(hero1.name)
print(hero1.__dict__)
print(hero1.health)
print(hero2.name)
