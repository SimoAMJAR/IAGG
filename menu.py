import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

class Menu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    def draw_game_over(self, score, high_score):
        self.screen.fill(BLACK)
        text = self.font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center=(200, 150))
        self.screen.blit(text, text_rect)

        score_text = self.font.render(f'Score: {score}', True, WHITE)
        score_rect = score_text.get_rect(center=(200, 250))
        self.screen.blit(score_text, score_rect)

        high_score_text = self.font.render(f'High Score: {high_score}', True, WHITE)
        high_score_rect = high_score_text.get_rect(center=(200, 350))
        self.screen.blit(high_score_text, high_score_rect)

        restart_text = self.font.render('Press R to Restart', True, WHITE)
        restart_rect = restart_text.get_rect(center=(200, 450))
        self.screen.blit(restart_text, restart_rect)

        quit_text = self.font.render('Press Q to Quit', True, WHITE)
        quit_rect = quit_text.get_rect(center=(200, 550))
        self.screen.blit(quit_text, quit_rect)

        pygame.display.flip()

    def draw_start(self, background_image):
        background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(background_image, (0, 0))

        # Define the pixelated font and size
        start_font = pygame.font.Font('PressStart2P-Regular.ttf', 18)  # Replace 'PressStart2P-Regular.ttf' with your font file
        # Render the text with neon glow effect
        start_text = start_font.render('Press Space to Start', True, (255, 255, 255))  # White color
        text_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        # Render the text with neon glow effect
        text_outline = start_font.render('Press Space to Start', True, (0, 0, 0))  # Black outline
        text_outline.set_alpha(100)  # Set transparency for the outline

        # Blit the text with outline to create a neon glow effect
        self.screen.blit(text_outline, text_rect.move(2, 2))  # Offset for the glow effect
        self.screen.blit(text_outline, text_rect.move(-2, -2))  # Offset for the glow effect
        self.screen.blit(text_outline, text_rect.move(2, -2))  # Offset for the glow effect
        self.screen.blit(text_outline, text_rect.move(-2, 2))  # Offset for the glow effect

        # Finally, render the actual text
        self.screen.blit(start_text, text_rect)

        pygame.display.flip()
