class Hero:
    def __init__(self, name, level, HP):
        self.name = name
        self.level = level
        self.HP = HP

    def is_adult(self):
        if int(self.level) >= 10:
            return True
        else:
            return False

    def introduce(self):
        return print(f'Привет, меня зовут {self.name}, мой lvl {self.level}, мое HP {self.HP}')

Pathfinder = Hero('PATHFINDER','11','800')
Wraith = Hero('WRAITH','5','600')
Octane = Hero('OCTANE','30','650')

Pathfinder.introduce()
Pathfinder.is_adult()
Wraith.introduce()
Wraith.is_adult()
Octane.introduce()
Octane.is_adult()