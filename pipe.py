import pygame
import random
from asset_manager import AssetManager

# Constants
PIPE_WIDTH = 90
MIN_PIPE_HEIGHT = 100
MAX_PIPE_HEIGHT = 600 - 250 - MIN_PIPE_HEIGHT  # Adjust as needed

class Pipe:
    def __init__(self, x, gap, asset_manager):
        self.x = x
        self.gap = gap
        self.height = random.randint(MIN_PIPE_HEIGHT, MAX_PIPE_HEIGHT)
        self.speed = 5

        self.bottom_image = asset_manager.images['pipe']
        self.top_image = asset_manager.images['pipe_flipped']

        self.top_rect = self.top_image.get_rect(midbottom=(self.x, self.height))
        self.bottom_rect = self.bottom_image.get_rect(midtop=(self.x, self.height + self.gap))

    def update(self):
        self.x -= self.speed
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        screen.blit(self.top_image, self.top_rect)
        screen.blit(self.bottom_image, self.bottom_rect)

    def off_screen(self):
        return self.x < -PIPE_WIDTH
