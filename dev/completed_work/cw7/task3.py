# Задание 3

class Point:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def coordinates(self):
        print(f'\nКоординаты точки: ({self.x1};{self.y1})')
        return self.x1, self.y1

    def p_and_s(self, x2, y2):
        x1 = self.x1
        y1 = self.y1

        s = abs((x2 - x1)*(y2 - y1))
        p = abs((x2 - x1)*2 + (y2 - y1)*2)

        print(f'\nПлощадь равна: {s}\nПериметр равен: {p}')
        return s, p


point = Point(4, 5)

point.coordinates()

point.p_and_s(1, 2)
