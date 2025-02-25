# Задание 2


class Chicken:
    def ceggs(self):
        return 30

    def iamchick(self):
        return "Я курица."


class Russian(Chicken):
    def ceggs(self):
        return 40

    def iamchick(self):
        return f'{super().iamchick()} Моя страна - Россия. Я несу {self.ceggs()} яиц в месяц.'


class Belarus(Chicken):
    def ceggs(self):
        return 23

    def iamchick(self):
        return f'{super().iamchick()} Моя страна - Белорусь. Я несу {self.ceggs()} яиц в месяц.'


class Moldova(Chicken):
    def ceggs(self):
        return 35

    def iamchick(self):
        return f'{super().iamchick()} Моя страна - Молдавия. Я несу {self.ceggs()} яиц в месяц.'
