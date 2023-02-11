from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, pi, radius):
        self.pi = pi
        self.radius = radius
        
    def area(self):
        return self.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * self.pi * self.radius
        
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * self.width + 2 * self.height

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5   
    def perimeter(self):
        return self.a + self.b + self.c
        

calculation = [
    
    Circle(3.14, 15),
    Rectangle(10, 5),
    Triangle(3, 4, 5)
    
]
    
for c in calculation:
    print(f"{c.__class__.__name__} Area: {c.area()} {c.__class__.__name__} Perimeter: {c.perimeter()}")
