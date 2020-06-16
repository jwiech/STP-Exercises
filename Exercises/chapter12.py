class Apple():
    def __init__(self, a, b, c, d):
        self.color = a
        self.weight = b
        self.type = c
        self.taste = d

import math
class Circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
circle = Circle(4)
print(circle.area())

class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return .5 * self.base * self.height
triangle = Triangle(3, 4)
print(triangle.area())

class Hexagon():
    def __init__(self, side):
        self.side = side
    def perimeter(self):
        return self.side * 6
hexagon = Hexagon(6)
print(hexagon.perimeter())
