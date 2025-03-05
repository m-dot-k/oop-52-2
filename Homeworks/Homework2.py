class Heroes:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return print(f'{self.name} достает оружие')

    def attack(self):
        return print(f'{self.name} атакует')


class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name,hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        self.arrows -= 1
        if self.precision > 50:
            return print(f'{self.name} совершает выстрел | Успешный выстрел | Кол-во стрел: {self.arrows}')
        else:
            return print(f'{self.name} совершает выстрел | Неудачный выстрел | Кол-во стрел: {self.arrows}')

    def rest(self):
        self.arrows += 5
        return print(f'Стрелы пополнились, текущее кол-во стрел = {self.arrows}')

    def status(self):
        return print(f' Name: {self.name} \n HP: {self.hp} \n arrows: {self.arrows} \n precision: {self.precision}')

Sova = Archer('Sova', 100, 10, 50)
Sova.status()
Sova.action()
Sova.attack()
Sova.rest()
Sova.status()