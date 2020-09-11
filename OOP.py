
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Square:
    def __init__(self,s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self,size):
        self.s1 += size



rect = Rectangle(1,1)
print(f"Area of Rectangle: {rect.calculate_perimeter()}")

squ = Square(2)
print(f"Area of square: {squ.calculate_perimeter()}")
