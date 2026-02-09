import pygame
from pygame.locals import *

class App:
    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((640,240),flags)
        App.t = Text("Pygame App", pos=(20,20))

        App.running = True

    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False

            App.t.draw()
            pygame.display.update()
            
        pygame.quit()

class Scene:
    id = 0
    bg = Color("gray")

    def __init__(self, *args, **kwargs):
        App.scenes.append(self)
        App.scene = self
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Scene.bg
    def draw(self):
        App.screen.fill(self.bg)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()
    def __str__(self):
        return "Scene {}".format(self.id)

class Text:
    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('white')
        self.set_font()
        self.render()

    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        App.screen.blit(self.img, self.rect)

if __name__=='__main__':
    App().run()
