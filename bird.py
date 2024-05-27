import pygame
from asset_manager import AssetManager

# Constants
GRAVITY = 1
FLAP_STRENGTH = -10

class Bird:
    def __init__(self, asset_manager):
        self.image = asset_manager.images['bird']
        self.rect = self.image.get_rect(center=(50, 300))
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)
