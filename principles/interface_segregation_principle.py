from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class ThreeDimensionalShape(Shape):
    @abstractmethod
    def calculate_volume(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length


class Cuboid(ThreeDimensionalShape):
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height

    def calculate_area(self):
        return 2 * (
            self.width * self.length
            + self.width * self.height
            + self.length * self.height
        )

    def calculate_volume(self):
        return self.width * self.length * self.height


""" This code snippet violates Interface Segregation Principle(ISP)
class Shape(ABC):    
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_volume(self):
        pass


class Square(Shape):
    def calculate_area(self):
        pass

    def calculate_volume(self):
        pass


class Rectangle(Shape):
    def calculate_area(self):
        pass 

    def calculate_volume(self):
        pass


class Cuboid(Shape):
    def calculate_area(self):
        pass 

    def calculate_volume(self):
        pass
"""
