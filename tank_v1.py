from time import sleep
import random
import os

field_size = 20
fuel = field_size / 2 
shot_count = 0
on_target = 0
hit = False
# tank_body = ['↑', '→', '↓', '←']
tank_body = ['^', '>', 'v', '<']
tank_rotation = 0
tank_x = 0
tank_y = 0
enemy_x = 0
enemy_y = 0
shot = False
tank_plus_enemy = True


def get_random_tank():
    global tank_x, tank_y, enemy_x, enemy_y, tank_rotation
    tank_plus_enemy = False
    while not tank_plus_enemy:
        tank_x = random.choice(range(field_size))
        tank_y = random.choice(range(field_size))
        enemy_x = random.choice(range(field_size))
        enemy_y = random.choice(range(field_size))
        tank_rotation = random.choice(range(len(tank_body)))
        tank_plus_enemy = tank_x != enemy_x and tank_y != enemy_y


def get_random_enemy():
    global tank_x, tank_y, enemy_x, enemy_y, tank_rotation
    tank_plus_enemy = False
    while not tank_plus_enemy:
        enemy_x = random.choice(range(field_size))
        enemy_y = random.choice(range(field_size))
        tank_plus_enemy = tank_x != enemy_x and tank_y != enemy_y


def display_field():
    global field_size, tank_body, tank_rotation, tank_x, tank_y, enemy_x, enemy_y, shot
    field = [['·' for _ in range(field_size)] for _ in range(field_size)]  # construct empty field
    for index_y, y in enumerate(field):
        for index_x, x in enumerate(y):
            if index_x == tank_x and index_y == tank_y:
                print(tank_body[tank_rotation], end=' ')
                continue
            elif shot and tank_rotation == 0 and index_y < tank_y and tank_x == index_x:  # shot north
                print('•', end=' ')
                continue
            elif shot and tank_rotation == 1 and index_x > tank_x and tank_y == index_y:  # shot east
                print('•', end=' ')
                continue
            elif shot and tank_rotation == 2 and index_y > tank_y and tank_x == index_x:  # shot south
                print('•', end=' ')
                continue
            elif shot and tank_rotation == 3 and index_x < tank_x and tank_y == index_y:  # shot west
                print('•', end=' ')
                continue
            elif index_x == enemy_x and index_y == enemy_y:  # show enemy
                print('O', end=' ')
                continue
            print('·', end=' ')
        print()


def display_header(fuel, shot_count, on_target):
    print('-' * ((field_size * 2) - 1))
    print(f'Fuel: {fuel} Shots: {shot_count} On target: {on_target}')
    print('-' * ((field_size * 2) - 1))


def display_footer():
    print('-' * ((field_size * 2) - 1))
    print(f'  w   |   ↑   | "w" - Forward, "s" - Backwards\n'
          f'a s d | ← ↓ → | "a" - Left,    "d" - Right    \n'
          f'                         "f" - Fire!          ')
    print('-' * ((field_size * 2) - 1))


def tank_action():
    global tank_body, tank_rotation, tank_y, tank_x, shot, shot_count, fuel, on_target, hit
    action = input('Your command: ')
    if action == 'd':
        tank_rotation += (1 if tank_rotation < 3 else -3)
    if action == 'a':
        tank_rotation -= (1 if tank_rotation > 0 else -3)
    if action == 'w' and tank_rotation == 0:  # North motion fwd
        tank_y -= (1 if tank_y > 0 else 0)
    if action == 'w' and tank_rotation == 1:  # East motion fwd
        tank_x += (1 if tank_x < field_size - 1 else 0)
    if action == 'w' and tank_rotation == 2:  # South motion fwd
        tank_y += (1 if tank_y < field_size - 1 else 0)
    if action == 'w' and tank_rotation == 3:  # West motion fwd
        tank_x -= (1 if tank_x > 0 else 0)

    if action == 's' and tank_rotation == 0:  # North motion back
        tank_y += (1 if tank_y < field_size - 1 else 0)
    if action == 's' and tank_rotation == 1:  # East motion back
        tank_x -= (1 if tank_x > 0 else 0)
    if action == 's' and tank_rotation == 2:  # South motion back
        tank_y -= (1 if tank_y > 0 else 0)
    if action == 's' and tank_rotation == 3:  # West motion back
        tank_x += (1 if tank_x < field_size - 1 else 0)
    if action == 'f':
        shot = True
        shot_count += shot
        if tank_rotation == 0 and tank_x == enemy_x and enemy_y < tank_y:
            hit = True
        elif tank_rotation == 1 and tank_y == enemy_y and enemy_x > tank_x:
            hit = True
        elif tank_rotation == 2 and tank_x == enemy_x and enemy_y > tank_y:
            hit = True
        elif tank_rotation == 3 and tank_y == enemy_y and enemy_x < tank_x:
            hit = True
        else:
            hit = False
    fuel -= 1


# Start
get_random_tank()
get_random_enemy()
while fuel >= 0:
    os.system('cls' if os.name == 'nt' else 'clear')  # refresh screen
    display_header(fuel, shot_count, on_target)
    display_field()
    display_footer()
    if shot:
        sleep(0.3)
        shot = False
        if hit:
            get_random_enemy()
            on_target += 1
            fuel += field_size / 2
            hit = False
        continue
    tank_action()
print('\n\nYou are out of fuel. And probably burned alive...\n\n')
