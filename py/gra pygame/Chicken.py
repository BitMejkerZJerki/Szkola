import pygame
from random import randint

class Chicken:
    def __init__(self):
        self.img = pygame.image.load("kura.png")
        self.pos = (randint(0,1200),randint(0,800)) 
        self.size = randint(70,150)
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos