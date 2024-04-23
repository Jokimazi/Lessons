# Задание 2

from random import randint


class Game:
    def __init__(self, max_num):
        self.max_num = max_num
        self.guesses = []
        self.target = randint(1, max_num)

    def play(self):
        print("Добро пожаловать в игру Угадай число!")
        while True:

            guess = int(input(f"\nПожалуйста, угадайте число от 1 до {self.max_num}: "))

            if guess == self.target:
                print("\nВы угадали правильное число! Поздравляю!")
                break

            elif guess in self.guesses:
                print("\nВы уже использовали это число.")

            elif guess > self.target:
                self.guesses.append(guess)
                print("\nВаше число больше правильного числа.")

            else:
                self.guesses.append(guess)
                print("\nВаше число меньше правильного числа.")


class EasyGame(Game):
    def __init__(self):
        super().__init__(10)


class MediumGame(Game):
    def __init__(self):
        super().__init__(100)


class HardGame(Game):
    def __init__(self):
        super().__init__(1000)


# Разные сложности игры
'''easy_game = EasyGame()
easy_game.play()

medium_game = MediumGame()
medium_game.play()'''

hard_game = HardGame()
hard_game.play()
