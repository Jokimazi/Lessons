# Задание 2

class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


number = Calc(12, 4)

print(number.addition())
print(number.subtraction())
print(number.multiplication())
print(number.division())
