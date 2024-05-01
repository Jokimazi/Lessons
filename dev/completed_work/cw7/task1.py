# Задание 1
# Что то я увлекся :/
# работоспособность можно проверить в консоли
# или просто запустив код

from colorama import init
import random

init()


class Item:
    # Инициализация класса
    def __init__(self,
                 ptype: str = '*****',
                 clas: str = '*****',
                 name: str = '*****',
                 critdmg: float = None,
                 critch: float = None,
                 damage: float = None,
                 buffspeed: float = None,
                 buffhealth: float = None,
                 buffhealth_max: float = None,
                 durability: int = -1,
                 description: str = None,
                 upgrade_name: str = None,
                 upgrade_name_color: str = ''):
        self.ptype = ptype
        self.clas = clas
        self.name = name
        self.critdmg = critdmg
        self.critch = critch
        self.damage = damage
        self.buffspeed = buffspeed
        self.buffhealth = buffhealth
        self.buffhealth_max = buffhealth_max
        self.durability = durability
        self.durability_max = self.durability
        self.description = description
        self.upgradelvl = 0
        self.upgrade_name = upgrade_name
        self.upgrade_name_color = upgrade_name_color

    # Выводит информацию о предмете
    def info(self):
        plus_spd = ''
        plus_maxh = ''
        plus_h = ''
        upgradelvl = '☆☆☆☆☆'

        if self.upgradelvl == 1:
            upgradelvl = '★☆☆☆☆'
        elif self.upgradelvl == 2:
            upgradelvl = '★★☆☆☆'
        elif self.upgradelvl == 3:
            upgradelvl = '★★★☆☆'
        elif self.upgradelvl == 4:
            upgradelvl = '★★★★☆'
        elif self.upgradelvl >= 5:
            upgradelvl = '★★★★★'

        if self.buffspeed is not None:
            if self.buffspeed >= 0:
                plus_spd = '+'

        if self.buffhealth is not None:
            if self.buffhealth >= 0:
                plus_h = '+'

        if self.buffhealth_max is not None:
            if self.buffhealth_max >= 0:
                plus_maxh = '+'

        if self.upgrade_name is not None:
            if self.upgradelvl == 5:
                self.name = self.upgrade_name_color + self.upgrade_name + '\033[0m'

        item_info = [self.name,
                     f'Тип: {self.ptype}',
                     f'Класс: {self.clas}',
                     f'Улучшение: {upgradelvl}',
                     f'Урон: {self.damage}',
                     f'Прочность: {self.durability}/{self.durability_max}',
                     f'Крит. урон: {self.critdmg}%',
                     f'Шанс к.у: {self.critch}%',
                     f'Бонусы:',
                     f' * {plus_maxh}{self.buffhealth_max} ед. макс. здоровья',
                     f' * {plus_h}{self.buffhealth} ед. здоровья',
                     f' * {plus_spd}{self.buffspeed} ед. скорости']

        if self.damage is None:
            item_info.remove(f'Урон: {self.damage}')

        if self.durability <= self.durability_max < 0:
            item_info[item_info.index(f'Прочность: {self.durability}/{self.durability_max}')] = 'Прочность: одноразовое'

        if self.durability == 0:
            item_info[item_info.index(f'Прочность: {self.durability}/{self.durability_max}')] += ' *cломан*'

        if self.critdmg is None or self.critch is None:
            item_info.remove(f'Крит. урон: {self.critdmg}%')
            item_info.remove(f'Шанс к.у: {self.critch}%')

        if self.ptype.split('/')[0] != 'оружие':
            item_info.remove(f'Улучшение: {upgradelvl}')

        a = 0

        if self.buffhealth_max is None:
            item_info.remove(f' * {plus_maxh}{self.buffhealth_max} ед. макс. здоровья')
            a += 1

        if self.buffhealth is None:
            item_info.remove(f' * {plus_h}{self.buffhealth} ед. здоровья')
            a += 1

        if self.buffspeed is None:
            item_info.remove(f' * {plus_spd}{self.buffspeed} ед. скорости')
            a += 1

        if a == 3:
            item_info.remove(f'Бонусы:')

        max_len = 0
        for i in item_info:
            if len(i) > max_len:
                max_len = len(i)

        # Вывод верхней рамки с именем, имя всегда будет по центру
        o = 0
        if self.upgrade_name is not None:
            o = len(self.upgrade_name_color) + 7
        inp = '\n╔'
        if max_len > len(self.name):
            names = ' ' + self.name + ' '
            names = names.center(max_len+2-o, '═')
            inp += names
            inp += '╗'
        else:
            inp += ' ' + self.name + ' ╗'
        print(inp)
        item_info.remove(self.name)

        # Выводим все строки информации
        for i in item_info:
            a = 0
            if i[:10] == 'Улучшение:':
                a = -2
            print('║ ' + i + ' '*(max_len-len(i)+a) + ' ║', end='\n')

        # Выводим описание (если оно не равно None)
        if self.description is not None:
            print('║ ' + ' '*max_len + ' ║')

            i = 0
            for i in range(0, len(self.description)-max_len, max_len):
                print('║ ' + self.description[i:i + max_len] + ' ║')

            ent = self.description[i+max_len:i + max_len*2]
            print('║ ' + ent + ' '*(max_len-len(ent)) + ' ║')

        # Выводим нижнюю рамку
        print('╚' + '═'*(max_len+2) + '╝')

    # Чинит предмет
    def repair(self, count: int = 0):
        if self.durability_max < 0:
            print(f'\n[Оповещение] Предмет "{self.name}" не поддается починке')
            return
        if count <= 0 or count > self.durability_max:
            self.durability = self.durability_max
        else:
            self.durability += count
        print(f'\n[Оповещение] Предмет "{self.name}" отремонтирован до {self.durability}/{self.durability_max} ед.')

    # Улучшает характереистики предмета
    def upgrade(self, addlvl):
        if self.ptype.split('/')[0] == 'оружие':
            self.upgradelvl += addlvl

            if self.upgradelvl > 5:
                self.upgradelvl = 5
            if self.upgradelvl < 0:
                self.upgradelvl = 0

            self.damage = round(self.damage * (1.15 ** self.upgradelvl), 1)
            self.critdmg = round(self.critdmg * (1.10 ** self.upgradelvl), 1)
            self.durability_max = round(self.durability_max * (1.07 ** self.upgradelvl))
            self.critch = round(self.critch * (1.05 ** self.upgradelvl), 1)

            print(f'\n[Оповещение] Предмет "{self.name}" был улучшен до уровня {self.upgradelvl}')
        else:
            print(f'\n[Оповещение] Предмет "{self.name}" не улучшаем')


class Entity:

    racedata = {'Человек': {'health': 20, 'damage': 1.5, 'speed': 7},
                'Орк': {'health': 30, 'damage': 4, 'speed': 4}}

    def __init__(self,
                 race: str = '***',
                 name: str = '***',
                 health: float = 0,
                 damage: float = 0,
                 speed: float = 0):

        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed
        self.race = race
        self.health_max = self.health
        self.slot = None

        if race in list(self.racedata.keys()):
            self.health = self.racedata[race]['health']
            self.damage = self.racedata[race]['damage']
            self.speed = self.racedata[race]['speed']
            self.health_max = self.health

    def attack(self, enemy):
        if self.health == 0:
            print(f'\n[Оповещение] {self.name} не может аттаковать, он мертв')
            return
        damage = 0
        critura = ''
        item = self.slot
        if self.slot is not None:
            if item.durability != 0:
                damage += item.damage
                item.durability = abs(item.durability) - 1
                if (item.critdmg or item.critch) is not None:
                    if item.critch > random.randint(1, 100):
                        damage *= (1+item.critdmg/100)
                        critura = '*КРИТ*'
        damage += self.damage
        damage = round(damage, 1)

        if enemy.health == 0:
            print(f'\n[Оповещение] {self.name} ударил труп')
            return

        enemy.health -= damage

        if enemy.health < 0:
            enemy.health = 0

        print(f'\n[Битва] {self.name} нанес {damage}{critura} едениц урона'
              f' персонажу {enemy.name}(HP: {round(enemy.health, 1)})')

        if enemy.health == 0:
            print(f'\n[Битва] {enemy.name} убит существом {self.name}')

        if item is not None:
            if item.durability == 0:
                print(f'\n[Оповещение] *хрусь* предмет в руке {self.name} сломан')
                self.drop_item_from_slot()

    def use_item(self, item):
        if self.health == 0:
            print(f'\n[Оповещение] {self.name} не может использовать предмет, он мертв')
            return

        if item.ptype.split('/')[0] != 'используемое':
            print(f'\n[Оповещение] {self.name} не может использовать предмет'
                  f' "{item.name}", он не являеться используемым')
            return

        if item.buffhealth_max is not None:
            self.health_max += item.buffhealth_max

        if item.buffhealth is not None:
            if self.health + item.buffhealth > self.health_max:
                self.health = self.health_max
            else:
                self.health += item.buffhealth

        if item.buffspeed is not None:
            self.speed += item.buffspeed
        print(f'\n[Оповещение] {self.name} использовал предмет "{item.name}"')

    def take_item_into_slot(self, item):
        if self.health == 0:
            print(f'\n[Оповещение] {self.name} не может взять предмет, он мертв')
            return

        if item.durability == 0:
            print(f'\n[Оповещение] предмет, который {self.name} пытаетется взять - сломан')
            return

        if item.ptype.split('/')[0] == 'оружие':
            item_prev = self.slot

            if item_prev is not None:
                if item_prev.buffhealth_max is not None:
                    self.health_max -= item_prev.buffhealth_max

                if item_prev.buffhealth is not None:
                    self.health -= item_prev.buffhealth

                if item_prev.buffspeed is not None:
                    self.speed -= item_prev.buffspeed

            self.slot = item

            if item.buffhealth_max is not None:
                self.health_max += item.buffhealth_max

            if item.buffhealth is not None:
                if self.health + item.buffhealth > self.health_max:
                    self.health = self.health_max
                else:
                    self.health += item.buffhealth

            if item.buffspeed is not None:
                self.speed += item.buffspeed

            print(f'\n[Оповещение] {self.name} взял в руки предмет "{self.slot.name}"')
        else:
            print(f'\n[Оповещение] {self.name} не может взять в руки предмет "{item.name}", он не являеться оружием ')

    def drop_item_from_slot(self):
        if self.health == 0:
            print(f'\n[Оповещение] {self.name} не может выкинуть предмет, он мертв')
            return
        item = self.slot
        if self.slot is None:
            print(f'\n[Оповещение] {self.name} руки пусты, он нечего не выкинул')
        else:
            print(f'\n[Оповещение] {self.name} выкинул предмет "{self.slot.name}"')

            if item.buffhealth_max is not None:
                self.health_max -= item.buffhealth_max

            if item.buffhealth is not None:
                self.health -= item.buffhealth

            if item.buffspeed is not None:
                self.speed -= item.buffspeed

            self.slot = None

    def revive(self):
        self.health = self.health_max
        print(f'\n[Оповещение] Существо под именем "{self.name}" было восскрешено')


bob = Entity('Человек', 'Боб')
ork = Entity('Орк', 'Угабуга')
admin_sword = Item('оружие/магический посох', 'легендарный', 'Посох всевластия', 9999, 9999, 9999, 9999, 9999, 9999)
elucidator = Item('оружие/меч', 'эпический', 'Вразумитель', 21, 34, 9.4, 6,
                  buffhealth_max=-4, durability=230,
                  description='Легендарный меч наиискуснейшего мечника всего Айнкрада')
apple = Item('используемое/еда', 'обычный', 'Яблоко', buffhealth=3,
             description='Когда-то оно упало на голову какому-то Ньютону')
golden_apple = Item('используемое/еда', 'легендарный', 'Яблоко нотча', buffhealth=15, buffhealth_max=3, buffspeed=5,
                    description='Когда-то оно выпало из какого-то игрока при убийстве :/')
dick = Item('оружие/член', 'эпохальный', 'Встанислав шишкин', 666, 228, 1488, durability=5,
            description='Оружие, хозяин которого был не кто иной, '
                        'как - Высунь Хуй Да Дай Подержать Другим. '
                        'Погиб при странных обстоятельствах, Встанислава нашли у него в жопе. '
                        'И теперь, разум Высунь Хуй Да Дай Подержать Другим перенесься в оружие,'
                        ' теперь, он ищет мести.',
            upgrade_name='Пизда ахилеса', upgrade_name_color='\033[1m\033[31m')

# Небольшой скрипт для проверки
elucidator.durability = 1
elucidator.info()

bob.take_item_into_slot(elucidator)
bob.attack(ork)

elucidator.info()

elucidator.repair(1)

ork.take_item_into_slot(elucidator)

ork.attack(bob)
ork.attack(bob)

ork.take_item_into_slot(elucidator)

ork.attack(bob)
ork.attack(bob)

bob.revive()

bob.use_item(admin_sword)
bob.take_item_into_slot(apple)

golden_apple.info()

ork.use_item(golden_apple)

elucidator.info()

elucidator.repair()
ork.take_item_into_slot(elucidator)
ork.attack(bob)

admin_sword.upgrade(5)
admin_sword.info()
bob.take_item_into_slot(admin_sword)
bob.attack(ork)

ork.revive()

elucidator.upgrade(3)
elucidator.info()

ork.take_item_into_slot(elucidator)
ork.attack(bob)

bob.revive()

dick.upgrade(5)

dick.info()

bob.take_item_into_slot(dick)

bob.attack(ork)
