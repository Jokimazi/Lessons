from task2 import *


class PoultryFarm:
    def __init__(self):
        self.__chicks = {
            'Россия': [],
            'Белорусь': [],
            'Молдавия': []
        }
        self.__bel = 0
        self.__rus = 0
        self.__mold = 0
        self.__total_eggs = 0
        self.__total_chick = 0

    def __create_russ(self):
        self.__chicks['Россия'].append(Russian())

    def __create_bel(self):
        self.__chicks['Белорусь'].append(Belarus())

    def __create_mold(self):
        self.__chicks['Молдавия'].append(Moldova())

    def generate_chicks(self, count, typo):
        for i in range(count):
            if typo == 'Россия':
                self.__create_russ()
            elif typo == 'Белорусь':
                self.__create_bel()
            elif typo == 'Молдавия':
                self.__create_mold()

    def get_count_rus(self):
        self.__rus = len(self.__chicks['Россия'])
        return self.__rus

    def get_count_bel(self):
        self.__bel = len(self.__chicks['Белорусь'])
        return self.__bel

    def get_count_mold(self):
        self.__mold = len(self.__chicks['Молдавия'])
        return self.__mold

    def get_total_eggs(self):
        for i in self.__chicks:
            for j in self.__chicks[i]:
                self.__total_eggs += j.ceggs()
        return self.__total_eggs

    def get_total_chick(self):
        for i in self.__chicks:
            self.__total_chick += len(self.__chicks[i])
        return self.__total_chick


P = PoultryFarm()

P.generate_chicks(25, 'Молдавия')
P.generate_chicks(60, 'Россия')
P.generate_chicks(40, 'Белорусь')

print(P.get_count_bel())
print(P.get_count_rus())
print(P.get_count_mold())

print(P.get_total_eggs())
print(P.get_total_chick())
