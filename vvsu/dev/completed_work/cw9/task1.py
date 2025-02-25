import math


class Shape:
    def __init__(self):
        self.per = None
        self.ar = None
        self.vol = None


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def __height(self):
        self._h = (self.a * self.b) / self.c

    def area(self):
        self.__height()
        self.ar = (self._h*self.c)/2
        return self.ar

    def volume(self):
        self.__height()
        self.vol = (self._h * self.c**2)/3
        return self.vol

    def perimeter(self):
        self.per = self.a + self.b + self.c
        return self.per


class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.__r = 0
        self.__d = self.__r*2
        self.__pi = math.pi

    def get_r(self):
        print('Вы получили доступ на чтение атрибута r')
        return self.__r

    def __diam(self):
        self.__d = self.__r * 2

    def set_r(self, val):
        print('Вы получили доступ на запись атрибута r')
        self.__r = val
        self.__diam()
        return self.__r

    def area(self):
        self.ar = math.pi * self.__r**2
        return self.ar

    def volume(self):
        self.vol = (4 * self.__pi * self.__r**3)/3
        return self.vol

    def perimeter(self):
        self.per = self.__pi * self.__d
        return self.per


tr = Triangle(2, 4, 5)

print(tr.area())
print(tr.perimeter())
print(tr.volume())

ci = Circle()

print(ci.volume())

print(ci.get_r())
print(ci.set_r(5))

print(ci.area())
print(ci.perimeter())
print(ci.volume())
