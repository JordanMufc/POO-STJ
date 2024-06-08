import pygame
import pytmx
import pyscroll

from screen import Screen
from player import Player
from npc import NPC
from keylistener import KeyListener


class Map:
    def __init__(self, screen: Screen, keylistener: KeyListener):
        self.screen = screen
        self.keylistener = keylistener
        self.tmx_data = None
        self.map_layer = None
        self.group = None
        self.player: Player = None

        self.collision: list[pygame.rect] = []
        self.switch_map('world')

    def add_player(self, player):
        self.player = player
        self.group.add(player)
        self.player.align_hitbox()

    def switch_map(self, map_name: str):
        self.tmx_data = pytmx.load_pygame(f'../assets/map/{map_name}.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.display.get_size())
        self.map_layer.zoom = 1
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)

        for obj in self.tmx_data.objects:
            if obj.name == 'collision':
                self.collision.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.name == 'NPC':
                sprite_name = obj.properties.get('graphic', 'default')
                sprite_path = f'../assets/sprites/Characters/{sprite_name}.png'  # Chemin d'accès au sprite
                npc = NPC(self.keylistener, self.screen, obj.x, obj.y, sprite_path)
                npc.direction = obj.properties.get('direction', 'down')
                self.add_player(npc)

    def update(self):
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.display)
