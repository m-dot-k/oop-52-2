
from abc import ABC, abstractmethod
import random

class Hero(ABC):

    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.__random_int = random.randint(1, 3)

    def attack(self):
        return print(f'{self.name} атакует')

    def protection(self):
        return print(f'{self.name} защищается')

    def rest(self):
        return print(f'{self.name} отдыхает')

    def get_random_int(self):
        return self.__random_int

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass

class Jester(Hero):
    def unique_attack(self):
        return print(f'{self.name} взрывает гранату')

    def unique_scream(self):
        return print(f'{self.name} издает боевой клич')

    def action(self):
        number = self.get_random_int()
        if number == 1:
            return self.attack()
        if number == 2:
            return self.protection()
        if number == 3:
            return self.rest()


Fuse = Jester('Fuse', 500, 10)
Fuse.get_random_int()
Fuse.unique_attack()
Fuse.unique_scream()
Fuse.action()

