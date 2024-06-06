import pygame


class Tool:
    #Divide the sprite sheet to have only one sprite at time
    @staticmethod
    def split_image(spritesheet : pygame.Surface, x, y, width, height):
        return spritesheet.subsurface(pygame.Rect(x, y, width, height))