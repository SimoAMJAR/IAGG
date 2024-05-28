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
        self.jump_sound = pygame.mixer.Sound('sounds/jump.mp3')
        self.jump_sound.set_volume(0.15)  # Set volume to 50%

    def flap(self):
        self.velocity = FLAP_STRENGTH
        self.jump_sound.play()

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)
