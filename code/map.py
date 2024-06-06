import pygame
import pytmx
import pyscroll

from screen import Screen
from player import Player

class Map:
    def __init__(self, screen : Screen):
        self.screen = screen
        self.tmx_data = None
        self.map_layer = None
        self.group = None

        self.switch_map('world')
        self.player: Player | None = None

    def add_player(self, player):
        self.player = player
        self.group.add(player)
        self.player.align_hitbox()
    def switch_map(self, map :  str):
        self.tmx_data = pytmx.load_pygame(f'../assets/map/{map}.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.display.get_size())
        self.map_layer.zoom = 3
        self.group = pyscroll.PyscrollGroup(map_layer = self.map_layer, default_layer = 7)

    def update(self):
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.display)