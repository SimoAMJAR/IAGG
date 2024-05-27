import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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

    def draw_start(self):
        self.screen.fill(BLACK)
        start_text = self.font.render('Press Space to Start', True, WHITE)
        start_rect = start_text.get_rect(center=(200, 300))
        self.screen.blit(start_text, start_rect)
        pygame.display.flip()
