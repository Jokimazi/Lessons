def deposit_final_profit(a: int = 30000, n: int = 1):

    if a < 30000:
        raise ValueError('параметр "a" принимает значение не менее 30000')
    if n < 1:
        raise ValueError('параметр "n" принимает значение не менее 1')

    b = a

    for i in range(1, n+1):

        percent = 0.3 * (a // 10000)
        if percent >= 5:
            percent = 5

        if i in range(1, 4):
            percent += 3
        elif i in range(4, 7):
            percent += 5
        elif i >= 6:
            percent += 2

        a += a*(percent/100)
        print(percent)
        print(a)
        print(b)

    return f'{round(a - b, 2)} Рублей'


print(deposit_final_profit(200000, 8))
