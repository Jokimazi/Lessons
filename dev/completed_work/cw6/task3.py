def prime_numbers(a: int, z: int):

    if a < 1:
        raise ValueError('параметр "a" принимает только целые положительные числа')
    if z < 1:
        raise ValueError('параметр "z" принимает только целые положительные значения')
    if a > z:
        raise ValueError('параметр "a" должен быть больше чем "a"')

    list_pn = []

    for i in range(a, z+1):
        x = 0
        for j in range(1, i+1):
            if i % j == 0:
                x += 1
        if x == 2:
            list_pn.append(i)
    return list_pn

print(prime_numbers(1, 120))
