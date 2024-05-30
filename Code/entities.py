from settings import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups):
        super().__init__(groups)

class Player(Entity):
    def __init__(self, pos, frames, groups):
        super().__init__(pos, frames, groups)
        self.image = pygame.Surface((16,16))
        self.image.fill('red')
        self.rect = self.image.get_frect(center = pos)

        self.direction = vector()

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector()
        if keys[pygame.K_z]:
            input_vector.y -=1
        if keys[pygame.K_s]:
            input_vector.y +=1
        if keys[pygame.K_q]:
            input_vector.x -=1
        if keys[pygame.K_d]:
            input_vector.x +=1
        self.direction = input_vector

    def move(self, dt):
        self.rect.center += self.direction * 125 * dt

    def update(self, dt):
        self.input()
        self.move(dt)