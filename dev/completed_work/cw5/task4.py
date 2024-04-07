# Задание 4
tuple1 = (11, 355, 23, 24, 0, 'del')  # Если убрать 'del' тогда кортеж отсортируеться

for i in tuple1:
    if not str(i).isnumeric():
        print(tuple1)
        exit('Кортеж остался неизменным')
tuple2 = tuple(sorted(tuple1))
print(f'{tuple1} -> {tuple2}')


