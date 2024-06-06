from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups , z = WORLD_LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.z = z
        self.hitbox = self.rect.inflate(-self.rect.width / 2, -60)

class BorderSprite(Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.copy()
class AnimatedSprite(Sprite):
    def __init__(self, pos, surf, frames, groups, z = WORLD_LAYERS['main']):
        self.frame_index, self.frames = 0 , frames
        super().__init__(pos, surf, frames[self.frame_index], groups, z)
    def animate(self, dt):
        self.famre_index += 4 * dt
        self.image = self.frames[int(self.frame_index %len(self.frames))]
    def update(self, dt):
        self.animate(dt)
