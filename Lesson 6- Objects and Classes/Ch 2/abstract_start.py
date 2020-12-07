# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints
from abc import ABC, abstractmethod
from math import pi as pi

# import ABC (abstract method class) from base class
class GraphicShape(ABC):

    # calls the __init__ of the abstract class
    def __init__(self):
        super().__init__()

    # use the abstract method decorator
    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    # override the calcArea method
    def calcArea(self):
        return pi*(self.radius**2)


class Rectangle(GraphicShape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    # override the calcArea method
    def calcArea(self):
        if (self.side1 == self.side2):
            print("square")
        return self.side1*self.side2


# g = GraphicShape()
# TypeError: Can't instantiate abstract class GraphicShape with abstract methods calcArea

c = Circle(10)
print(c.calcArea())
r = Rectangle(12, 12)
print(r.calcArea())
