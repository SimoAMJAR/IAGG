import pygame
from bird import Bird
from pipe import Pipe
from menu import Menu

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAVITY = 1
FLAP_STRENGTH = -10

def get_speed(score):
    if score <= 15:
        return 5
    elif 16 <= score <= 40:
        return 8
    elif 41 <= score <= 60:
        return 12
    else:
        return 16

def get_gap(score):
    if score <= 15:
        return 250
    elif 16 <= score <= 40:
        return 240
    elif 41 <= score <= 60:
        return 230
    else:
        return 210

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird with Rectangles")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 55)

    # Load background image
    background_image = pygame.image.load('images/background.jpg')
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    game_started = False
    initial_start = True

    while running:
        bird = Bird()
        score = 0
        game_over = False

        # Initialize pipes with the initial gap
        gap = get_gap(score)
        pipes = [Pipe(SCREEN_WIDTH + i * (70 + gap), gap) for i in range(3)]

        menu = Menu(screen, font)
        if initial_start:
            menu.draw_start()

        while not game_started:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_started = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_started = True
                        initial_start = False

        while not game_over and running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.flap()

            bird.update()
            for pipe in pipes:
                pipe.update()
                if pipe.off_screen():
                    pipes.remove(pipe)
                    score += 1
                    # Update gap based on the new score
                    gap = get_gap(score)
                    pipes.append(Pipe(SCREEN_WIDTH, gap))

                if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                    game_over = True

            if bird.rect.top > SCREEN_HEIGHT:
                game_over = True  # Bird went below the screen

            # Get current speed based on score
            current_speed = get_speed(score)

            # Update pipes' speed
            for pipe in pipes:
                pipe.speed = current_speed

            screen.blit(background_image, (0, 0))
            bird.draw(screen)
            for pipe in pipes:
                pipe.draw(screen)

            score_surf = font.render(f'Score: {score}', True, WHITE)
            screen.blit(score_surf, (10, 10))

            pygame.display.flip()
            clock.tick(FPS)

        if not running:
            break

        menu.draw_game_over()

        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_over = False
                        game_started = True  # Restart directly without showing the start screen
                    if event.key == pygame.K_q:
                        running = False
                        game_over = False

    pygame.quit()

if __name__ == "__main__":
    main()
