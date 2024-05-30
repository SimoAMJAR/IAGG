import pygame

class AssetManager:
    def __init__(self):
        self.images = {}
        self.masks = {}
        self.load_assets()

    def load_assets(self):
        # Load images
        self.images['background'] = pygame.image.load('images/background1.png')
        self.images['bird'] = pygame.image.load('images/bird.png').convert_alpha()
        self.images['pipe'] = pygame.image.load('images/pipe1.png').convert_alpha()

        # Create masks for collision detection
        self.masks['bird'] = pygame.mask.from_surface(self.images['bird'])
        self.masks['pipe'] = pygame.mask.from_surface(self.images['pipe'])

        # Scale images as needed
        self.images['background'] = pygame.transform.scale(self.images['background'], (400, 600))
        self.images['pipe'] = pygame.transform.scale(self.images['pipe'], (90, self.images['pipe'].get_height()))
        self.images['pipe_flipped'] = pygame.transform.flip(self.images['pipe'], False, True)
        self.masks['pipe_flipped'] = pygame.mask.from_surface(self.images['pipe_flipped'])
