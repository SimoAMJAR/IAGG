import pygame
import random

# Constants
PIPE_WIDTH = 90
GAP = 200
PIPE_SPEED = 5
SCREEN_HEIGHT = 600
MIN_PIPE_HEIGHT = 100
MAX_PIPE_HEIGHT = SCREEN_HEIGHT - GAP - MIN_PIPE_HEIGHT

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(MIN_PIPE_HEIGHT, MAX_PIPE_HEIGHT)
        
        self.bottom_image = pygame.image.load('images/r.png')
        self.top_image = pygame.image.load('images/r.png')
        
        self.top_image = pygame.transform.flip(self.top_image, False, True)
        
        self.top_rect = self.top_image.get_rect(midbottom=(self.x, self.height))
        self.bottom_rect = self.bottom_image.get_rect(midtop=(self.x, self.height + GAP))

    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        screen.blit(self.top_image, self.top_rect)
        screen.blit(self.bottom_image, self.bottom_rect)

    def off_screen(self):
        return self.x < -PIPE_WIDTH