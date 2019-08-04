import pygame
import os
from enemies.scorpion import Scorpion
import time

class Game:
    def __init__(self):
        self.width = 1000
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = [Scorpion()]
        self.towers = []
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("..", "game_assets", "support_towers",  "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))

        for en in self.enemys:
            en.draw(self.win)

        pygame.display.update()


g = Game()
g.run()