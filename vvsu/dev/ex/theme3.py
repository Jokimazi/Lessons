for i in range(3):
   print(f'Студент №{i + 1}') 

for i in [0, 1, 2]:
   print(f'Студент №{i + 1}') 

for i in range(10, 1, -1):
   print(i)

for i in [10, 9, 8, 7, 6, 5, 4, 3, 2]:
   print(f'Студент №{i + 1}')

phrase = 'Фраза'

for i in phrase:
   print(i)

for i in ['Ф', 'р', 'а', 'з', 'а']:
   print(i)

for i in range(len(phrase)):
   print(i)
   print(phrase[i])

for i, letter in enumerate(phrase):
   print(i, letter)

n = 0
while n < 10:
   res = n * 2
   print(res)
   n += 1

for i in range(10):
   for j in range(10):
      print(i, j)

# Составьте программу, выводящую на экран квадраты чисел от 10 до 20.
for i in range(10, 21):
   print(f'Квадрат числа {i}: {i ** 2}' )

# Составьте программу, котораЯ вычисляет сумму чисел от 1 до n.значение n вводится с клавиатуры.
n = int(input('Введите число: '))
summa = 0

for i in range(1, n + 1):
   summa += i

print(f'Сумма равна {summa}')

# В сберкассу на трёхпроцентный вклад положили S рублей. Какой станет сумма вклада через N лет.

s, n = map(int, input('Ввидите сумму вклада и срок в годах: ').split())

procent = 0.03

for i in range(n):
   s = s + s * procent

print(s)
