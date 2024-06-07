import pygame
from entity import Entity
from keylistener import KeyListener
from screen import Screen
from tools import Tool
from settings import *

class NPC(Entity):
    def __init__(self, keylistener: KeyListener, screen: Screen, x: int, y: int, sprite_path: str):
        print("NPC initialized with arguments:", keylistener, screen, x, y, sprite_path)
        super().__init__(keylistener, screen, x, y)

        self.spritesheet = pygame.image.load(sprite_path)
        self.image = Tool.split_image(self.spritesheet, 0, 0, CHARACTER_SPRITE_WIDTH, CHARACTER_SPRITE_HEIGHT)
        self.all_images = self.get_all_images()
        self.index_image = 0
        self.image_part = 0
        self.reset_animation = False
        self.step = 0
        self.animation_walk = False
        self.direction = 'down'  
        self.walk_speed = 1
        self.animation_step_time = 0.0
        self.action_animation = 1

    def update(self):
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom
        self.image = self.all_images[self.direction][self.index_image]

    def load_sprite(self, sprite_name: str):
        # Charger le sprite correspondant au nom spécifié
        sprite_path = f'../assets/sprites/Characters/{sprite_name}.png'
        self.spritesheet = pygame.image.load(sprite_path)

    def set_sprite(self, sprite_name: str):
        # Définir le sprite pour ce PNJ en chargeant le sprite correspondant au nom spécifié
        self.load_sprite(sprite_name)
        # Mettre à jour toutes les images avec le nouveau sprite chargé
        self.all_images = self.get_all_images()    

    def get_all_images(self):
        all_images = {
            "down": [],
            "left": [],
            "right": [],
            "up": []
        }

        width = self.spritesheet.get_width() // 4
        height = self.spritesheet.get_height() // 4

        for i in range(4):
            for j, key in enumerate(all_images.keys()):
                all_images[key].append(Tool.split_image(self.spritesheet, i * width, j * height, width, height))
        return all_images
