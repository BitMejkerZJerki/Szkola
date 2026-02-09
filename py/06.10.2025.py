import random

class Gracz:
    def __init__(self):
        self.HP = 100
        self.ATK = 25
        self.DEF = 10

def Gatak(self, enemy):
    Edef = random.randint(1, 5)
    if Edef == 2 or Edef == 3:
        print("Unik")
    else:
        obrazenia = max(0, self.ATK - enemy.DEF)
        enemy.HP -= obrazenia
        print("Hp enemy" + str(enemy.HP))

class Enemy:
    def __init__(self):
        self.HP = 100
        self.ATK = 25
        self.DEF = 10

def atak(self, gracz):
    Pdef = random.randint(1, 5)
    if Pdef == 2 or Pdef == 3:
        print("Unik")
    else:
        obrazenia = max(0, self.ATK - gracz.DEF)
        gracz.HP -= obrazenia
        print("Hp gracza" + str(gracz.HP))

gracz = Gracz()
enemy = Enemy()

a = 0
while gracz.HP > 0 and enemy.HP > 0:
    if a == 0:
        gracz.Gatak(enemy)
        a = 1
    else:
        enemy.atak(gracz)
        a = 0

    if gracz.HP <= 0 and enemy.HP <= 0:
        print("Remis")
    elif gracz.HP <= 0:
        print("Enemy wygrywa")
    else:
        print("Gracz wygrywa")
