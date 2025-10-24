from math import pi
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod    
    def perimeter(self): pass
    def describe(self):
        return f"{self.__class__.__name__}(area={self.area():.3f}, perimeter={self.perimeter():.3f})"
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius **2 *pi
    
    def perimeter(self):
        return self.radius *2 *pi
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width + self.height) * 2
    
shape = [Circle(3), Rectangle(2.0, 3.0)]

print("\n=== 계산 결과 ===")
for s in shape:
    print(s.describe())
print("\n")