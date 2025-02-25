# Задание 3

while True:
    enter = input('\nВведите возраст собаки для конвертации в человеческий (1 - 22 лет): ')

    if enter.isdigit() or (enter[1:].isdigit() and enter[1:] == '-'):

        enter = int(enter)

        if enter < 1:
            print(f'\nОшибка: собаке, которой {enter} лет, это еще не родившаяся собака')
        elif enter > 22:
            print('\nОшибка: собаки столько не живут')
        elif enter <= 2:
            age = enter * 10.5
            print(f'\nВозрст собаки в человеческих годах: {age}')
            exit()
        else:
            enter -= 2
            age = 21 + enter * 4
            print(f'\nВозрст собаки в человеческих годах: {age}')
            exit()
    else:
        print('\nОшибка: неверный ввод')
