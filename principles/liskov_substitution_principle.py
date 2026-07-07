class Shape:
    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Rectangle(Shape):
    def set_width(self, width):
        self.width = width

    def set_length(self, length):
        self.length = length

    def get_area(self):
        return self.width * self.length


class Square(Shape):
    def set_side(self, side):
        self.side = side

    def get_area(self):
        return self.side**2


shape = Shape()
shape.set_color("Red")
print(shape.get_color())

rectangle = Rectangle()
rectangle.set_color("Red")
print(rectangle.get_color())

square = Square()
square.set_color("Red")
print(square.get_color())


""" This code snippet violates Liskov Substitution Principle(LSP)
class Rectangle:
    def set_width(self, width):
        self.width = width

    def set_length(self, length):
        self.length = length

    def set_color(self, color):
        self.color = color

    def get_area(self):
        return self.width * self.length
    

class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.length = width

    def set_height(self, length):
        self.width = length
        self.length = length


square = Square()
square.set_width(10)
square.set_length(5)
print(square.get_area())
"""
