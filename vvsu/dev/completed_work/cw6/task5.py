# Задание 5

def is_palindrome(a: str):
    a = ''.join(a.split()).lower()
    b = a[::-1]

    if a == b:
        return True
    else:
        return False


print(is_palindrome('А роза упала на лапу Азора'))
