import pygame
from random import randint
from pygame.locals import *
from Chicken import *
 
w = 1240
h = 740
 
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
 
targets = [Chicken(), Chicken()]
 
 
tlo = pygame.image.load("tlo.png")
cel = pygame.image.load("celownik.png")
 
rect_shooter = cel.get_rect()
rect_shooter.center = pygame.mouse.get_pos()
 
timer = 0
isRunning = True
pygame.mouse.set_visible(False)
 
while isRunning:
    timer += 1
    screen.blit(tlo, (0,0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:
                isRunning = False
 
        if event.type == MOUSEMOTION:
            rect_shooter.move_ip(event.rel)
 
        for target in targets:
            if event.type == MOUSEBUTTONDOWN and target.rect.collidepoint(rect_shooter.center):
                targets.remove(target)
 
    if timer == 100:
        targets.append(Chicken())
        timer = 0
 
    for target in targets:
        screen.blit(target.img, target.rect)
 
    screen.blit(cel, rect_shooter)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()  