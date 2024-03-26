# class Student():
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name

#     def sleep(self):
#         print(f'{self.name} спит')


# student1 = Student(20, 'Алексей')
# print(student1.age)
# student1.sleep()
# print(id(student1))

# print('\n')

# student2 = Student(23, 'Мария')
# print(student2.age)
# student2.sleep()
# print(id(student2))

import random

class Player():
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg
        self.hp = 100
    
    def heal(self):
        medicine = random.randint(1, 30)
        self.hp = self.hp + medicine

        print(f'Здоровье {self.name} увеличено на {medicine}')
        print(f'Здоровье {self.name}: {self.hp}')

        if self.hp >= 100:
            self.hp = 100

    def heat(self, enemy):
        enemy.hp = enemy.hp - self.dmg

        print(f'Нанесено {self.dmg} урона по {enemy.name}')
        print(f'Здоровье {enemy.name}: {enemy.hp}')

        if enemy.hp <= 0:
            print(f'{enemy.name} мертв')


player1 = Player('Алексей', 23)
player2 = Player('Мария', 40)

while True:
    move = random.choice([player1, player2])
    action = random.choice(['heal', 'heat'])

    if move == player1 and action == 'heal':
        player1.heal()
    
    if move == player2 and action == 'heal':
        player1.heal()

    if move == player1 and action == 'heat':
        player1.heat(player2)

        if player2.hp <= 0:
            print(f'{player1.name} победил')
            break
    
    if move == player2 and action == 'heat':
        player2.heat(player1)

        if player1.hp <= 0:
            print(f'{player2.name} победил')
            break
