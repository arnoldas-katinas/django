from time import sleep
import random
import os

class TankGame:
    def __init__(self, field_size=20):
        self.field_size = field_size
        self.fuel = field_size / 2
        self.tank_body = ['^', '>', 'v', '<']
        self.shot_count = 0
        self.on_target = 0
        self.hit = False
        self.tank_x, self.tank_y, self.enemy_x, self.enemy_y = 0, 0, 0, 0
        self.tank_rotation = 0
        self.shot = False

    def get_random_tank(self):
        self.tank_x, self.tank_y = random.choice(range(self.field_size)), \
                random.choice(range(self.field_size))
        self.tank_rotation = random.choice(range(len(self.tank_body)))

    def get_random_enemy(self):
        self.enemy_x, self.enemy_y = random.choice(range(self.field_size)), \
                random.choice(range(self.field_size))
        

    def display_field(self):
        for y in range(self.field_size):
            for x in range(self.field_size):
                if (x, y) == (self.tank_x, self.tank_y):
                    print(self.tank_body[self.tank_rotation], end=' ')
                elif (x, y) == (self.enemy_x, self.enemy_y):
                    print('O', end=' ')
                elif self.shot:
                    if self.tank_rotation == 0 and y < self.tank_y and x == self.tank_x:
                        print('•', end=' ')
                        continue
                    elif self.tank_rotation == 1 and x > self.tank_x and y == self.tank_y:
                        print('•', end=' ')
                        continue
                    elif self.tank_rotation == 2 and y > self.tank_y and x == self.tank_x:
                        print('•', end=' ')
                        continue
                    elif self.tank_rotation == 3 and x < self.tank_x and y == self.tank_y:
                        print('•', end=' ')
                        continue
                    else:
                        print('·', end=' ')
                else:
                    print('·', end=' ')
            print()

    def display_header(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # refresh screen
        print('-' * ((self.field_size * 2) - 1))
        print(f'Fuel: {self.fuel} Shots: {self.shot_count} On target: {self.on_target}')
        print('-' * ((self.field_size * 2) - 1))

    def display_footer(self):
        print('-' * ((self.field_size * 2) - 1))
        print(f'  w   |   ↑   | "w" - Forward, "s" - Backwards\n'
              f'a s d | ← ↓ → | "a" - Left,    "d" - Right    \n'
              f'                         "f" - Fire!          ')
        print('-' * ((self.field_size * 2) - 1))
        if self.shot: sleep(0.2)

    def tank_action(self):
        action = input('Your command: ')
        if action == 'd':
            self.tank_rotation = (self.tank_rotation + 1) % 4
        elif action == 'a':
            self.tank_rotation = (self.tank_rotation - 1) % 4
        elif action == 'w':
            if self.tank_rotation == 0:  # North motion
                self.tank_y = max(self.tank_y - 1, 0)
            elif self.tank_rotation == 1:  # East motion
                self.tank_x = min(self.tank_x + 1, self.field_size - 1)
            elif self.tank_rotation == 2:  # South motion
                self.tank_y = min(self.tank_y + 1, self.field_size - 1)
            elif self.tank_rotation == 3:  # West motion
                self.tank_x = max(self.tank_x - 1, 0)
        elif action == 's':
            if self.tank_rotation == 0:  # South motion
                self.tank_y = min(self.tank_y + 1, self.field_size - 1)
            elif self.tank_rotation == 1:  # West motion
                self.tank_x = max(self.tank_x - 1, 0)
            elif self.tank_rotation == 2:  # North motion
                self.tank_y = max(self.tank_y - 1, 0)
            elif self.tank_rotation == 3:  # East motion
                self.tank_x = min(self.tank_x + 1, self.field_size - 1)
        elif action == 'f':
            self.shot = True
            self.shot_count += 1
            if (self.tank_rotation == 0 and self.tank_x == self.enemy_x and self.enemy_y < self.tank_y) or \
               (self.tank_rotation == 1 and self.tank_y == self.enemy_y and self.enemy_x > self.tank_x) or \
               (self.tank_rotation == 2 and self.tank_x == self.enemy_x and self.enemy_y > self.tank_y) or \
               (self.tank_rotation == 3 and self.tank_y == self.enemy_y and self.enemy_x < self.tank_x):
                self.on_target += 1
                self.hit == True
                self.fuel += self.field_size / 2
                play.get_random_enemy()
        self.fuel -= 1

#    def run_game(self):
#        self.get


play = TankGame(field_size=16)

play.get_random_enemy()
play.get_random_tank()

while play.fuel >= 0:
    play.display_header()
    play.display_field()
    play.display_footer()
    if play.shot:
        play.shot = False
        continue
    play.tank_action()
    # play.run_game()
