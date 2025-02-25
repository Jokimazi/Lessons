# Задание 2

choose = int(input('\nВведите номер месяца, чтобы узнать к какому сезону он пренадлежит: '))

if choose in (1, 2, 12):
    print(f'\n{choose} месяц пренадлежит зимнему сезону')
elif choose in range(3, 6):
    print(f'\n{choose} месяц пренадлежит весеннему сезону')
elif choose in range(6, 9):
    print(f'\n{choose} месяц пренадлежит летнему сезону')
elif choose in range(9, 12):
    print(f'\n{choose} месяц пренадлежит осеннему сезону')
else:
    print(f'\nМесяца под номером {choose} еще не придумали(')

