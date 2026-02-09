import pygame
from pygame.locals import *
import random

pygame.init()

w = 1080
h = 720

cel = pygame.image.load("celownik.png")
rect = cel.get_rect()
screen = pygame.display.set_mode((w, h))
tlo = pygame.image.load("tlo.png")
enemy = (50, 20, 120, 100)
obiekty = [(50, 20, 120, 100), (450, 500, 120, 100), (700, 240, 120, 100)]
obiekty.append(enemy)

isRunning = True

while isRunning:
    screen.blit(tlo, (0, 0))
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:
                isRunning = False
        
        if event.type == MOUSEMOTION:
            rect.center = pygame.mouse.get_pos()

        for obj in obiekty:
            if event.type == MOUSEBUTTONDOWN and pygame.Rect.colliderect(rect, obj):
                obiekty.remove(obj)

    if len(obiekty) == 1:
        new_enemy = (random.randint(0, w - 120), random.randint(0, h - 100), 120, 100)
        obiekty.append(new_enemy)

    for obj in obiekty:
        pygame.draw.rect(screen, (255, 0, 0), obj)

    screen.blit(cel, rect)

    pygame.display.flip()
    pygame.display.update()

    if len(obiekty) == 0:
        isRunning = False

pygame.quit()
