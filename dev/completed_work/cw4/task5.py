enter = input('Введите пароль для проверки его на надежность: ')

for i in enter:
    if i.isupper():
        a = True
    else:
        print('Ваш пароль не надежный, добавьте заглавные буквы')
        exit()
    if i.islower():
        b = True
    else:
        print('Ваш пароль не надежный, добавьте строчные буквы')
        exit()
    if i.isdigit():
        c = True
    else:
        print('Ваш пароль не надежный, добавьте цифры')
        exit()
    if not set(".,:;!_*-+()/#¤%&)").isdisjoint(i):
        d = True
    else:
        print('Ваш пароль не надежный, добавьте спец символы')
        exit()
if a and b and c and d:
    print('Ваш пароль надежный')
