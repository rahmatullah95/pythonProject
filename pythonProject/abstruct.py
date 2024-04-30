from abc import ABC, abstractmethod

class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def area(self):
        area = .5 * self.dim1 * self.dim2
        print("Area of triangle is: ", area)

class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of rectangle is: ", area)

t = Triangle(23,45)
t.area()

r = Rectangle(23,45)
r.area()