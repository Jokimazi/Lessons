t = True # 1
f = False # 0

a = 4
b = 6

if a > b:
    print(f'Сумма равна {a + b}')

if a < b:
    print(f'Произведение равно {a * b}')

k = 5
t = 3

if k == t:
    print('Переменные равны')
else:
    print('Переменные не равны')

if k > t:
    print('k больше t')
elif k < t:
    print('k меньше t')
elif k == t:
    print('k равно t')
else:
    print('Ошибка')

n = 100

if n < 100:
    print(n ** 2)
elif n < 50:
    print(n ** 3)
elif n > 20:
    print(n)

# Болезнь       Родители   Не пошли на пары

# True    and   True       True
# True    and   False      False
# False   and   True       False
# False   and   False      False


# Голова        Сердце     Крит. урон

# True    or    True       True
# True    or    False      True   
# False   or    True       True
# False   or    False      False

import random

krit = 20
damage = random.randint(0, 100)

head = random.randint(0, 1)
heart = random.randint(0, 1)

print(f'krit: {krit}, damage: {damage}, head: {head}, heart: {heart}')

if head and damage > krit:
    print('Критическое попадание в голову')
if heart and damage > 50:
    print('Критическое попадание в сердце')

print('\n')

if head or heart:
    if head:
        print('Есть критическое попадание в голову')
    if heart:
        print('Есть критическое попадание в сердце')

if not a > b:
    print(a + b)
            
if a < b or k == t and a > b:
    print('Условие сработало')
