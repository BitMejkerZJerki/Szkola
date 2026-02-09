import pygame
from pygame.locals import *
import random 

pygame.init()

# Ustawienia ekranu
w, h = 1240, 800
screen = pygame.display.set_mode((w, h))

# Wczytanie tła i jego skalowanie
tlo = pygame.image.load("tlo.png")
tlo = pygame.transform.scale(tlo, (w, h))

# Wczytanie celownika
cel = pygame.image.load("celownik.png")
cel = pygame.transform.scale(cel, (50, 50))  # Pomniejszenie celownika
rect = cel.get_rect()

# Wczytanie obrazu kaczki
kaczka_img = pygame.image.load("kura.png")
kaczka_img = pygame.transform.scale(kaczka_img, (120, 100))

# Tworzenie początkowej kaczki w losowej pozycji
kaczka = {
    "x": random.randint(0, w - 120),
    "y": random.randint(0, h - 100),
    "speed_x": random.choice([-3, 3]),  # Losowy ruch w poziomie
    "speed_y": random.choice([-3, 3])   # Losowy ruch w pionie
}

isRunning = True

while isRunning:
    screen.blit(tlo, (0, 0))  # Rysowanie tła
    
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False
        
        if event.type == KEYDOWN:
            if event.key == K_q:
                isRunning = False
        
        if event.type == MOUSEMOTION:
            rect.center = event.pos 
        
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Lewy przycisk myszy
                kaczka_rect = pygame.Rect(kaczka["x"], kaczka["y"], 120, 100)
                if kaczka_rect.colliderect(rect):  # Sprawdzenie trafienia
                    # Tworzenie nowej kaczki w losowej pozycji
                    kaczka = {
                        "x": random.randint(0, w - 120),
                        "y": random.randint(0, h - 100),
                        "speed_x": random.choice([-3, 3]),
                        "speed_y": random.choice([-3, 3])
                    }
    
    # Aktualizacja pozycji kaczki
    kaczka["x"] += kaczka["speed_x"]
    kaczka["y"] += kaczka["speed_y"]
    
    # Odbicie kaczki od krawędzi ekranu
    if kaczka["x"] <= 0 or kaczka["x"] >= w - 120:
        kaczka["speed_x"] *= -1  # Zmiana kierunku poziomego
    if kaczka["y"] <= 0 or kaczka["y"] >= h - 100:
        kaczka["speed_y"] *= -1  # Zmiana kierunku pionowego
    
    # Rysowanie kaczki
    screen.blit(kaczka_img, (kaczka["x"], kaczka["y"]))
    
    # Rysowanie celownika
    screen.blit(cel, rect)
    
    # Aktualizacja ekranu
    pygame.display.flip()
    
pygame.quit()