class Example:
    def __init__(self):
        self.x = 0
        self._y = 1
        self.__z = 2

    def get_z(self):
        print('Вы получили доступ на чтение атрибута z')
        return self.__z

    def set_z(self, value):
        self.__z = value
        print(f'Атрибуту z присвоено новое значение: {self.__z}')

    def __calc(self):
        return self.x + self._y + self.__z
    
    def repres(self):
        print(f'Значение x: {self.x}')
        print(f'Значение y: {self._y}')
        print(f'Значение z: {self.__z}')
        print(f'Сумма: {self.__calc()}')


ex = Example()
print(ex.get_z())
ex.set_z(10)
print(ex.get_z())

ex.repres()


class StudentHouse:
    def __init__(self, bugs, emigrants):
        self.__bugs = bugs
        self.emigrants = emigrants
        self.rooms = 3

    def kill_bugs(self, poison):
        alive_bugs = self.__bugs - self.__bugs * poison // 100
        print(f'Померло {self.__bugs - alive_bugs} тараканов')

    def cook_karry(self):
        print(f'Воздух загрязнён на {self.emigrants / 10}')

    def get_bugs(self):
        return self.__bugs

    def set_bugs(self, count):
        self.__bugs = count


st = StudentHouse(666, 123)


st.kill_bugs(30)
st.cook_karry()
print(st.get_bugs())
st.set_bugs(3)
print(st.get_bugs())
