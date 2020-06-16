class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def perimeter(self):
        return self.length * 2 + self.width * 2
class Square():
    def __init__(self, side):
        self.side = side
    def perimeter(self):
        return self.side * 4
    def change_size(self,change):
        self.side = self.side + change
rectangle = Rectangle(5, 8)
square = Square(7)
print(rectangle.perimeter())
print(square.perimeter())
square.change_size(4)
print(square.perimeter())

class Shape():
    def what_am_i(self):
        print("I am a shape")
class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def perimeter(self):
        return self.length * 2 + self.width * 2
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def perimeter(self):
        return self.side * 4
    def change_size(self,change):
        self.side = self.side + change
rectangle = Rectangle(5, 8)
square = Square(7)
rectangle.what_am_i()
square.what_am_i()

class Horse():
    def __init__(self, age, sex, rider):
        self.age = age
        self.sex = sex
        self.rider = rider
class Person():
    def __init__(self, name):
        self.name = name
jockey = Person("John")
horse = Horse(4, "M", jockey)
print(horse.rider.name)
