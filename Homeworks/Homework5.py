class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return print (f'➜ Прямоугольник (ширина: {self.width}, высота: {self.height}')

    def __area__(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.width * self.height == other.height * other.width

    def __lt__(self, other):
        return self.width * self.height < other.height * other.width

    def __gt__(self, other):
        return self.width * self.height > other.height * other.width

r1 = Rectangle(4, 5)
r2 = Rectangle(3, 6)

