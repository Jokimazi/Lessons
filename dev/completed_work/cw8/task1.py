# Задание 1

class Animals:
    def __init__(self, name, sex, age, species):
        self.name = name
        self.sex = sex
        self.age = age
        self.species = species

    def eat(self):
        pass

    def move(self):
        pass

    def sleep(self):
        pass


class Birds(Animals):
    def __init__(self, name, sex, age, species, beak_size, wingspan):
        super().__init__(name, sex, age, species)
        self.beak_size = beak_size
        self.wingspan = wingspan

    def fly(self):
        pass

    def make_nest(self):
        pass

    def carry_eggs(self):
        pass


class Mammals(Animals):
    def __init__(self, name, sex, age, species, length_wool, color_wool):
        super().__init__(name, sex, age, species)
        self.length_wool = length_wool
        self.color_wool = color_wool

    def feed_milk_babies(self):
        pass

