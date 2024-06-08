import pygame
from screen import Screen
from map import Map
from keylistener import KeyListener
from player import Player

class Game:
    def __init__(self):
        self.running = True
        self.screen = Screen()
        self.keylistener = KeyListener()
        self.map = Map(self.screen, self.keylistener)
        self.player = Player(self.keylistener, self.screen, 800, 1550)
        self.map.add_player(self.player)


    def run(self):
        while self.running:
            self.handle_input()
            self.map.update()
            self.screen.update()


    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.keylistener.add_key(event.key)
            elif event.type == pygame.KEYUP:
                self.keylistener.remove_key(event.key)