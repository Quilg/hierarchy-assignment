
class Circle:
    def __init__(self, pi, radius):
        self.pi = pi
        self.radius = radius
        
    def area(self):
        return self.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * self.pi * self.radius
        
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * self.width + 2 * self.height

class Triangle:
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
    if isinstance(c, Circle):
        print("Circle Area:", c.area(), "Circle Perimeter:", c.perimeter())
    elif isinstance(c, Rectangle):
        print("Rectangle Area:", c.area(), "Rectangle Perimeter:", c.perimeter())
    elif isinstance(c, Triangle):
        print("Triangle Area:", c.area(), "Triangle Perimeter:", c.perimeter())