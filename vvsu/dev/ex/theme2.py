word = 'Слово'
char = '3'
word2 = "Word"
phrase = 'Слово содержит 5 букв'

a = 5
b = 2
res = a + b

print('Результат сложения', a, 'и', b, 'равен', res)
print(f'Результат сложения {a} и {b} равен {a + b}')

print(word + ' ' + word2)

# Слово
print(word.count('во'))
print(word.find('о'))
num = '234'
print(num.isdigit())
print(word.islower())
changed_word = word.upper()
print(changed_word)
print(changed_word.isupper())
print(word.replace('во', ''))

print(phrase.split('о'))

a, b, c = map(int, input('Введите три числа: ').split())
print(a + b + c)

print(word * 3)

print(word[1:])
print(word[1:3])
print(word[:4])
print(word[1:4:2])
print(word[::-1])

# "Слово"
#  01234
