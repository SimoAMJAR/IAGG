import pygame

# Constants
SCREEN_HEIGHT = 600
GROUND_HEIGHT = 100
BLACK = (0, 0, 0)

class Ground:
    def __init__(self):
        self.rect = pygame.Rect(0, SCREEN_HEIGHT - GROUND_HEIGHT, 400, GROUND_HEIGHT)

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect)