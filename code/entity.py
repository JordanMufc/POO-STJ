import pygame

from tools import Tool
from settings import *
from keylistener import KeyListener
from screen import Screen

class Entity(pygame.sprite.Sprite):
    def __init__(self, keylistener: KeyListener, screen: Screen, x : int, y: int):
        super().__init__()
        self.screen: Screen = screen
        self.keylistener = keylistener
        self.spritesheet = pygame.image.load('../assets/sprites/Characters/player.png')
        self.image = Tool.split_image(self.spritesheet,0, 0, CHARACTER_SPRITE_WIDTH,CHARACTER_SPRITE_HEIGHT)
        self.position : pygame.math.Vector2 = pygame.math.Vector2(x+TILES_SIZE, y)
        self.rect: pygame.Rect = self.image.get_rect()
        self.all_images = self.get_all_images()
        self.index_image: int = 0
        self.image_part: int = 0
        self.reset_animation = False
        self.hitbox: pygame.Rect = pygame.Rect(0, 0, TILES_SIZE, TILES_SIZE)

        self.step: int = 0
        self.animation_walk: bool = False
        self.direction = 'down'

        self.walk_speed: int = 1
        self.animation_step_time: float = 0.0
        self.action_animation = 1

    def update(self):
        self.animation_sprite()
        self.move()
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom
        self.image = self.all_images[self.direction][self.index_image]



    def move_left(self):
        self.animation_walk = True
        self.direction = 'left'
    def move_right(self):
        self.animation_walk = True
        self.direction = 'right'
    def move_up(self):
        self.animation_walk = True
        self.direction = 'up'
    def move_down(self):
        self.animation_walk = True
        self.direction = 'down'

    def animation_sprite(self):
        if int(self.step // 8) + self.image_part >= 4:
            self.image_part = 0
            self.reset_animation = True
        self.index_image = int(self.step // 8 ) + self.image_part

    # Entity move tile by tile and arnt affected by framerates
    def move(self):
        if self.animation_walk:
            self.animation_step_time += self.screen.deltatime
            if self.step < TILES_SIZE and self.animation_step_time >= self.action_animation:
                self.step += 1
                if self.direction == 'left':
                    self.position.x -= self.walk_speed
                elif self.direction == 'right':
                    self.position.x += self.walk_speed
                elif self.direction == 'up':
                    self.position.y -= self.walk_speed
                elif self.direction == 'down':
                    self.position.y += self.walk_speed
                self.animation_step_time = 0
            elif self.step >= 16:
                self.step = 0
                self.animation_walk = False
                if self.reset_animation:
                    self.reset_animation = False
                else:
                    if self.image_part == 0:
                        self.image_part = 2
                    else:
                        self.image_part = 0

    def align_hitbox(self):
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.x % TILES_SIZE != 0:
            self.rect.x -= 1
            self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.y % TILES_SIZE != 0:
            self.rect.y -= 1
            self.hitbox.midbottom = self.rect.midbottom
        self.position = pygame.math.Vector2(self.rect.center)

    def get_all_images(self):
        all_images = {
            "down": [],
            "left": [],
            "right": [],
            "up": []
        }

        width: int = self.spritesheet.get_width() // 4
        height: int = self.spritesheet.get_height() // 4

        for i in range(4):
            for j, key in enumerate(all_images.keys()):
                all_images[key].append(Tool.split_image(self.spritesheet, i * width, j* height, width, height))
        return all_images