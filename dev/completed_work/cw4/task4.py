# Задание 4

enter = input('Ведите число: ')
summ = 0
a = ''

if enter.isdigit() or (enter[1::].isdigit() and enter[0] == '-'):
    if enter[1::].isdigit() and enter[0] == '-':
        enter = enter[1::]
        a = '-'
    for i in enter:
        summ += int(i)
    if summ % 3 == 0 and int(enter[-1]) % 2 == 0:
        print(f'Число {a}{enter} делиться на 6 нацело и равно {a}{round(int(enter)/6)}')
    else:
        print(f'Число {a}{enter} не делиться на 6 нацело')

else:
    print('Ошибка: неверный ввод')