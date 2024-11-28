##일반화관계

import math
from abc import ABC, abstractmethod

# class Shape:
#     @abstractmethod
#     def area(self):
#         # raise NotImplementedError("Subclasses must implement this method.")
#         pass
class Shape(ABC):
    @abstractmethod
    def area(self):
        # raise NotImplementedError("Subclasses must implement this method.")
        pass
       
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height #사각형의 면적
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

shapes = [
    Triangle(3,4),
    Rectangle(5,2),
    Circle(3)
]
for shape in shapes:
    print(f"The area is: {shape.area()}")