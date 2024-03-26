def greetings(name, surname=''):
    # name = input('Введите имя: ')
    print(f'Welcome {name} {surname}!')
    print('🥳')

def add(x, y):
    res = x + y
    return res / 2

def newfunc(n):
    def myfunc(x):
        return x + n

    return myfunc

def factorial(k):
    if k < 0:
        return 0
    if k == 0:
        return 1
    
    return k * factorial(k - 1)

# 3! 1 * 2 * 3
print(factorial(3))

new = newfunc(100)
print(new(200))

names = ['Alex', 'Mary', 'John']
surname = 'Smith'

for name in names:
    greetings(name, surname)

result = add(5, 3)
print(result)

print(add(10, 3))

print(greetings('Kate'))

def bsearch(list, idx0, idxn, val):

    if (idxn < idx0):
        return None
    else:
        midval = idx0 + ((idxn - idx0) // 2)

        if list[midval] > val:
            return bsearch(list, idx0, midval - 1, val)
        elif list[midval] < val:
            return bsearch(list, midval+1, idxn, val)
        else:
            return midval

list = [8, 11, 24, 56, 88, 131, 145, 180, 200, 211, 231, 246, 267, 289, 290]

print(bsearch(list, 0, 5, 11))
# print(bsearch(list, 0, 5, 51))

def func(*args):
    print(args[4])

def an_func(**kwargs):
    print(kwargs['b'])

func(3, 34, 5, 2, 5, 6, 3, 6, 1)
an_func(a=1, b=2, c=5, d=10)

def isRectangular(x1, y1, x2, y2, x3, y3):
    a = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2
    b = abs(x2 - x3) ** 2 + abs(y2 - y3) ** 2
    c = abs(x1 - x3) ** 2 + abs(y1 - y3) ** 2

    if (a == b + c) or (b == a + c) or (c == a + b):
        print('YES')
    else:
        print('NO')

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

isRectangular(x1, y1, x2, y2, x3, y3)
