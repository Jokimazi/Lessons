class Shape:
    def __init__(self):
        self.per = None
        self.area = None
        self.vol = None


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.h = (a*b)/c

    def area(self):
        self.area = (self.h*self.c)/2
        return self.area

    def volume(self):
        self.vol = (self.h * self.c**2)/3
        return self.vol

    def perimeter(self):
        self.per = self.a + self.b + self.c
        return self.per


