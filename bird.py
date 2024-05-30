import pygame
from asset_manager import AssetManager

# Constants
GRAVITY = 1
FLAP_STRENGTH = -10
FLYING_DURATION = 0.2  # Duration in seconds for flying animation

class Bird:
    def __init__(self, asset_manager):
        self.images = {
            'normal': asset_manager.images['bird'],
            'flying': asset_manager.images['flying']  # Assuming you have an image for the flying bird
        }
        self.rect = self.images['normal'].get_rect(center=(50, 300))
        self.velocity = 0
        self.mask = pygame.mask.from_surface(self.images['normal'])
        self.jump_sound = pygame.mixer.Sound('sounds/jump.mp3')
        self.jump_sound.set_volume(0.15)  # Set volume to 15%
        self.flap_time = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH
        self.jump_sound.play()
        self.flap_time = pygame.time.get_ticks()  # Record the time of the flap

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

        # Check if flying animation time has elapsed
        if pygame.time.get_ticks() - self.flap_time < FLYING_DURATION * 1000:
            self.image = self.images['flying']
        else:
            self.image = self.images['normal']

    def draw(self, screen):
        screen.blit(self.image, self.rect)
