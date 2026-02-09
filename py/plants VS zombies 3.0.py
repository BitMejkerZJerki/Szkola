import random

class Player():
    def __init__(self):
        Player.HP = 5
        Player.CASH = 100
        Player.TIME = 0

class Enemy():
    def __init__(self, x, y):
        Enemy.NAME = "Slawko"
        Enemy.ICON = "┗|｀O′|┛"
        Enemy.HP = 5
        Enemy.SPEED = 1
        Enemy.VALUE = 25
        Enemy.x = x
        Enemy.y = y

Enemy()


def createMap(x,y):
    tab = []
    tab1 = []
    for yi in range(y):
        tab1.append(["[ ]"])

    for xi in range(x):
        tab.append(tab1)
    return tab


WIDTH = int(input("Podaj szerokosc mapy >> "))
HEIGHT = int(input("Podaj wysokosc mapy >> "))
print(Enemy.ICON)

tab = createMap(HEIGHT, WIDTH)
for x in tab:
    for y in x:
        print(y[0], end="")
    print()


enemy_x = WIDTH-1
enemy_y = random.randint(0, HEIGHT-1)
enemy = Enemy(enemy_x, enemy_y)
tab[enemy_x, enemy_y] = Enemy.ICON

for row in tab:
    for cell in row:
        print(cell, end="")
    print()
