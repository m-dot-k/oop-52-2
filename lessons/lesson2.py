"""Наследование"""

#Предок, суперкласс, базовый класс
class Hero:

    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduce(self):
        return print(f'Я {self.name}, мой уровень {self.lvl}')

    def action(self):
        return print(f'{self.name} выполняет базовое действие')

#Потомок, подкласс, класс-наследник
class Warrior(Hero): #CamalCase - верблюжья нотация (UpperCamalCase & lowerCamalCase)
    def __init__(self,name,lvl,hp,stamina):
        super().__init__(name,lvl,hp)
        self.stamina = stamina

    def attack(self):
        if self.stamina >= 10:
            self.stamina -= 1
            return print(f'{self.name} атакует мечом')
        else:
            return print(f'У {self.name} мало стамины')

    def introduce(self): # полиморфизм
        return print('Izmenilsya')

class Mage(Hero):
    def __init__(self, name, lvl, hp, mana):
        super().__init__(name,lvl,hp)
        self.mana = mana

iso = Warrior('Iso',100,1000,50) #SnakeCase - змеиная нотация
iso.action()
iso.introduce()
iso.attack()
sage = Mage('Sage',200,500,100)
sage.action()
sage.introduce()

"""Константные переменные"""
# К ним можно обращаться из любого места кода
URL = '123.123.123'
ADMIN = "Maksim"