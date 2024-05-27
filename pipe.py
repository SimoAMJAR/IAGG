import pygame
import random

# Constants
PIPE_WIDTH = 90
GAP = 250
MIN_PIPE_HEIGHT = 100
MAX_PIPE_HEIGHT = 600 - GAP - MIN_PIPE_HEIGHT
PIPE_SPEED = 5

class Pipe:
    def __init__(self, x, gap):
        self.x = x
        self.height = random.randint(MIN_PIPE_HEIGHT, MAX_PIPE_HEIGHT)
        self.speed = PIPE_SPEED
        self.gap = gap
        
        self.bottom_image = pygame.image.load('images/r.png')
        self.top_image = pygame.image.load('images/r.png')
        
        self.bottom_image = pygame.transform.scale(self.bottom_image, (PIPE_WIDTH, self.bottom_image.get_height()))
        self.top_image = pygame.transform.scale(self.top_image, (PIPE_WIDTH, self.top_image.get_height()))
        self.top_image = pygame.transform.flip(self.top_image, False, True)
        
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
