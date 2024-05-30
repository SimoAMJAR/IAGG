import pygame
import random
from asset_manager import AssetManager

# Constants
PIPE_WIDTH = 90
MIN_PIPE_HEIGHT = 100
MAX_PIPE_HEIGHT = 600 - 250 - MIN_PIPE_HEIGHT  # Adjust as needed
PIPE_VERTICAL_SPEED = 2  # Speed at which pipes move up and down

class Pipe:
    def __init__(self, x, gap, asset_manager, score):
        self.x = x
        self.gap = gap
        self.height = random.randint(MIN_PIPE_HEIGHT, MAX_PIPE_HEIGHT)
        self.speed = 5
        self.vertical_speed = PIPE_VERTICAL_SPEED if score > 60 else 0  # Start vertical movement after score 60
        self.vertical_direction = 1  # 1 means down, -1 means up

        self.bottom_image = asset_manager.images['pipe']
        self.top_image = asset_manager.images['pipe_flipped']

        self.top_rect = self.top_image.get_rect(midbottom=(self.x, self.height))
        self.bottom_rect = self.bottom_image.get_rect(midtop=(self.x, self.height + self.gap))

        self.top_mask = pygame.mask.from_surface(self.top_image)
        self.bottom_mask = pygame.mask.from_surface(self.bottom_image)

    def update(self):
        self.x -= self.speed
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

        if self.vertical_speed:
            self.height += self.vertical_speed * self.vertical_direction
            if self.height > MAX_PIPE_HEIGHT or self.height < MIN_PIPE_HEIGHT:
                self.vertical_direction *= -1  # Change direction
            self.top_rect.midbottom = (self.x, self.height)
            self.bottom_rect.midtop = (self.x, self.height + self.gap)

    def draw(self, screen):
        screen.blit(self.top_image, self.top_rect)
        screen.blit(self.bottom_image, self.bottom_rect)

    def off_screen(self):
        return self.x < -PIPE_WIDTH

    def get_collision(self, bird):
        if self.top_rect.colliderect(bird.rect):
            offset = (bird.rect.left - self.top_rect.left, bird.rect.top - self.top_rect.top)
            if self.top_mask.overlap(bird.mask, offset):
                return True
        if self.bottom_rect.colliderect(bird.rect):
            offset = (bird.rect.left - self.bottom_rect.left, bird.rect.top - self.bottom_rect.top)
            if self.bottom_mask.overlap(bird.mask, offset):
                return True
        return False
