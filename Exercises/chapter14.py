class AlwaysPositive:
    def __init__(self, number):
    	self.r = number
    def __add__(self, other):
        return abs(self.r + other.r)
x = AlwaysPositive(-20)
y = AlwaysPositive(10)
print(x+y)

class Square():
    square_list = []
    def __init__(self, side):
        self.side = side
        self.square_list.append(self)
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)
    def perimeter(self):
        return self.side * 4
    def change_size(self,change):
        self.side = self.side + change
Square(10)
Square(20)
print(Square.square_list)

def same_obj_check(obj1, obj2):
    return obj1 is obj2
sq1 = Square(12)
sq2 = sq1
sq3 = Square(12)
print(same_obj_check(sq1, sq2))
print(same_obj_check(sq1, sq3))
