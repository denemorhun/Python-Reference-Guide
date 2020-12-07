# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod
import json

class JSONify(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def toJSON(ABC):
        pass

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return "Radius to Area -> {" + f" {self.radius} : {str(self.calcArea())}" + "}"

circles = []
c1 = Circle(10)
c2 = Circle(15)
c3 = Circle(20) 

circles.append(c1) 
circles.append(c2)
circles.append(c3)

for c in circles:
    print(c.calcArea())
    print(c.toJSON())
