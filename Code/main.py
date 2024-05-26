from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join, abspath, dirname


from sprites import Sprite

class Game: 
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDHT, WINDOW_HEIGHT))
        pygame.display.set_caption('Le donjon de Barleroi')

        # Create Group or Groups
        self.all_sprites = pygame.sprite.Group()

        self.import_assets()
        self.setup(self.tmx_maps['world'], 'ground')
        

    def import_assets(self):
        self.tmx_maps = {'world': load_pygame(os.path.abspath('Data/Maps/World.tmx'))}

    def setup(self, tmx_map, player_start_pos):
         for x,y, surf in tmx_map.get_layer_by_name('ground').tiles():
            Sprite((x * TILE_SIZE,y * TILE_SIZE), surf, self.all_sprites)


    def run(self):
        while True:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # game logic
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
