class Hero:
    def __init__(self, name, health, attackPower) -> None:
        self.__name = name
        self.__health = health
        self.__attackpower = attackPower

    # getter
    def getName(self):
        return self.__name

    def getHelath(self):
        return self.__health

    # setter
    def diserang(self, serangPower):
        self.__health -= serangPower

    def setAttackPower(self, nilaiBaru):
        self.__attackpower = nilaiBaru


earthshaker = Hero("earthshaker", 50, 5)

print(earthshaker.__dict__)

# game berjalan

# earthshaker.__name = "windrunner"
print(earthshaker.getName())
print(earthshaker.getHelath())
earthshaker.diserang(5)
print(earthshaker.getHelath())
