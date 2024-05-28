import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

class Menu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    def draw_game_over(self, score, high_score, background_image):
        self.screen.blit(background_image, (0, 0))  # Draw the background image

        # Render and apply neon glow effect to "Game Over" text
        self.render_with_neon_glow('Game Over', (SCREEN_WIDTH // 2, 150))

        # Render and apply neon glow effect to "Score" text
        score_text = f'Score: {score}'
        self.render_with_neon_glow(score_text, (SCREEN_WIDTH // 2, 250))

        # Render and apply neon glow effect to "High Score" text
        high_score_text = f'High Score: {high_score}'
        self.render_with_neon_glow(high_score_text, (SCREEN_WIDTH // 2, 350))

        # Render and apply neon glow effect to "Press R to Restart" text
        self.render_with_neon_glow('Press R to Restart', (SCREEN_WIDTH // 2, 450))

        # Render and apply neon glow effect to "Press Q to Quit" text
        self.render_with_neon_glow('Press Q to Quit', (SCREEN_WIDTH // 2, 550))

        pygame.display.flip()

    def render_with_neon_glow(self, text, center):
        # Render the text with neon glow effect
        text_surface = self.font.render(text, True, (255, 255, 255))  # White color
        text_rect = text_surface.get_rect(center=center)

        # Render the text with neon glow effect
        text_outline = self.font.render(text, True, (0, 0, 0))  # Black outline
        text_outline.set_alpha(100)  # Set transparency for the outline

        # Blit the text with outline to create a neon glow effect
        self.screen.blit(text_outline, text_rect.move(2, 2))  # Offset for the glow effect
        self.screen.blit(text_outline, text_rect.move(-2, -2))  # Offset for the glow effect
        self.screen.blit(text_outline, text_rect.move(2, -2))  # Offset for the glow effect
        self.screen.blit(text_outline, text_rect.move(-2, 2))  # Offset for the glow effect

        # Finally, render the actual text
        self.screen.blit(text_surface, text_rect)

        pygame.display.flip()

    def draw_score(self, score):
        # Render the score using the pixelated font with neon glow effect
        score_text = f'Score: {score}'
        score_surface = self.font.render(score_text, True, (255, 255, 255))  # White color
        score_rect = score_surface.get_rect(topleft=(75, 12))  # Position in the top left corner
        self.render_with_neon_glow(score_text, (score_rect.x, score_rect.y))  # Apply neon glow effect

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
