import pygame

# Constants
GRAVITY = 1
FLAP_STRENGTH = -10

class Bird:
    def __init__(self):
        self.image = pygame.image.load('images/cropped_bird.png')
        self.rect = self.image.get_rect(center=(50, 300))
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)