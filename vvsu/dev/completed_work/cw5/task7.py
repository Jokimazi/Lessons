# Задание 7
dict_eng_rus = {
    'call': 'звонить',
    'cyborg': 'киборг',
    'city': 'город',
    'russia': 'россия',
    'weapon': 'оружие'
}

enter = input('Введите русское слово для перевода: ')

for eng, rus in dict_eng_rus.items():
    if rus == enter:
        print(f'"{enter}" на англиском будет: {eng}')
        exit()
print(f'Перевода для слова "{enter}" в словаре нет')