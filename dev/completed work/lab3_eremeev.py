# Задание 1
name = input('Введите имя: ')
age = input('Введите возраст: ')

for i in range(10):
    print(f'{i+1}. Меня зовут {name}, мне {age} лет')

# Задание 2
num = int(input('\nВведите цифру: '))

print(f'Таблица умножения на {num}:')
for i in range(1, 10):
    print(f'{num} x {i} = {num*i}')
print('')

# Задание 3
'''Я до конца не понял задания, от 0 включительно или нет,
 здесь: 0 - первое, 1 - второе, 2 - третье, 4 - первое и т.д.'''
for i in range(0, 101, 2):
    print(i)

# Задание 4
num = int(input('\nВведите число: '))
a = 1

for i in range(1, num+1):
    a *= i
print(f'Факториал числа {num} равен {a}\n')

# Задание 5
num = 20
while num != -1:
    print(num)
    num -= 1

# Задание 6
num = int(input('\nВведите число: '))
fir, sec, summ = 1, 0, 0

while sec < num:
    thi = fir + sec
    fir, sec = sec, thi
    print(fir)

# Задание 7
enter = input('\nВведите слово: ')

for i in range(len(enter)):
    print(f'{i+1}{enter[i]}', end='')

# Задание 8
while True:
    num1, num2 = map(int, input('\n\nВведите два числа через пробел: ').split())
    print('Сумма равна:', num1+num2)
