from settings import *
from os.path import join
from os import walk
from pytmx.util_pygame import load_pygame


def import_image (*path, alpha = True, format = 'png'):
    full_path = join (*path) + f'.{format}'
    surf = pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert()
    return surf

def import_tilemap(cols, rows, *path):
    frames = {}
    surf = import_image(*path)
    cell_width, cell_height = surf.get_width() / cols, surf.get_height() / rows
    for col in range (cols):
            for row in range(rows):
                 cutout_rect = pygame.Rect(col * cell_width, row * cell_height, cell_width, cell_height)
                 cutout_surf = pygame.Surface((cell_width, cell_height))
                 cutout_surf.fill('green')
                 cutout_surf.set_colorkey('green')
                 cutout_surf.blit(surf, (0,0), cutout_rect)
                 frames[(col, row)] = cutout_surf

def import_folder(*path):
    frames = []
    for folder_path, sub_folders, image_names in walk (join(*path)):
        for image_name in sorted(image_name, key = lambda name: int (name.split('.')[0])):
            full_path = join(folder_path, image_name)
            surf = pygame.image.load(full_path).convert_alpha()
            frames.append(surf)
    return frames

def import_folder_dict(*path):
    frames = {}
    for folder_path, sub_folders, image_names in walk(join(*path)):
        for image_name in image_names:
            full_path = join(folder_path, image_name)
            surf = pygame.image.load(full_path).convert_alpha()
            frames[image_name.split('.')[0]] = surf

def import_sub_folder(*path):
    frames = {}
    for _, sub_folders, __ in walk(join(*path)):
        if sub_folders:
            for sub_folder in sub_folders:
                frames[sub_folder] = import_folder(*path, sub_folder)
    return frames

def character_importer(cols, rows, *path):
    frame_dict = import_tilemap(cols, rows, *path)
    new_dict = {}
    for row, direction in enumerate (('down', 'left', 'right', 'up')):
        new_dict[direction] = [frame_dict[(col, row)] for col in range(cols)]
        new_dict[f'{direction}_idle'] = [frame_dict[(0,row)]]
    return new_dict

def all_character_import(*path):
    new_dict = {}
    for _, __, image_names in walk(join(*path)):
        for image in image_names:
            image_name = image.split('.')[0]
            new_dict[image_name] = character_importer(4,4,*path, image_name)
    return new_dict