# Задание 5
while True:
    a = False
    b = False
    c = False
    d = False
    e = True
    f = True

    enter = input('Введите пароль для проверки его на надежность: ')

    error = '\nВаш пароль не надежный, пароль должен содержать: '
    eng_lang = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    spec_chars = "@#$%^&*()_+=<>?-,./!`~':;|\"\\№]}{["

    for i in enter:
        if i.isalpha():
            if not (i in eng_lang):
                e = False
        if i.isupper():
            a = True
        if i.islower():
            b = True
        if i.isdigit():
            c = True
        if i in spec_chars:
            d = True
    if len(enter) < 8:
        f = False
    if a and b and c and d and e and f:
        print('\nВаш пароль надежный!')
        exit()
    else:
        if not a:
            error += 'заглавные буквы, '
        if not b:
            error += 'строчные буквы, '
        if not c:
            error += 'цифры, '
        if not d:
            error += 'спец символы, '
        if not e:
            error += 'только латинские буквы, '
        if not f:
            error += 'не менее 8 символов, '
        print(error[:-2] + '.')
