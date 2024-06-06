import pygame
from settings import *

class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('RPG project game')
        self.clock = pygame.time.Clock()
        self.deltatime: float = 0.0

    # Method used to redraw the screen every frames
    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(FRAMES_RATES)
        self.display.fill(0)
        self.deltatime = self.clock.get_time()