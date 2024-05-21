# decorator getter setter
class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.__info = "name {} : \n\thealth: {}".format(self.__name, self.__health)

    @property
    def info(self):
        return "name {} : \n\thealth: {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print("armor di delete")
        self.__armor = None


sniper = Hero("sniper", 100, 10)


print("merubah info")
# print(sniper.info)
# sniper.info = "info"
print(sniper.info)
sniper.name = "dadang"
print(sniper.info)


print("getter dan setter untuk armor")
print(sniper.armor)
# sniper.armor = 10
sniper.armor = 50
print(sniper.armor)
print(sniper.armor)

print("delete armor")
del sniper.armor
