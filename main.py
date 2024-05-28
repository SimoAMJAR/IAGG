import pygame
from bird import Bird
from pipe import Pipe
from menu import Menu
from asset_manager import AssetManager

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 30
WHITE = (255, 255, 255)

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

def load_high_score():
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def save_high_score(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

def countdown(screen, font, bird, pipes, background):
    for i in range(3, 0, -1):
        screen.blit(background, (0, 0))  # Draw the background
        bird.draw(screen)  # Draw the bird
        for pipe in pipes:
            pipe.draw(screen)  # Draw the pipes

        countdown_text = font.render(str(i), True, WHITE)
        text_rect = countdown_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(countdown_text, text_rect)
        pygame.display.flip()
        pygame.time.delay(1000)  # Delay for 1 second

def draw_pause_message(screen, font, background, bird, pipes):
    screen.blit(background, (0, 0))  # Draw the background
    bird.draw(screen)  # Draw the bird
    for pipe in pipes:
        pipe.draw(screen)  # Draw the pipes

    pause_text = font.render("Pause", True, WHITE)
    text_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(pause_text, text_rect)
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird with Rectangles")
    clock = pygame.time.Clock()
    
    # Load fonts
    pixel_font = pygame.font.Font('PressStart2P-Regular.ttf', 18)  # Load the pixelated font

    asset_manager = AssetManager()
    high_score = load_high_score()

    running = True
    game_started = False
    initial_start = True
    paused = False

    while running:
        bird = Bird(asset_manager)
        score = 0
        game_over = False

        gap = get_gap(score)
        pipes = [Pipe(SCREEN_WIDTH + i * (70 + gap), gap, asset_manager, score) for i in range(3)]

        menu = Menu(screen, pixel_font)  # Use the pixelated font for the menu
        if initial_start:
            menu.draw_start(asset_manager.images['background'])

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
                    elif event.key == pygame.K_ESCAPE:
                        paused = not paused
                        if paused:
                            draw_pause_message(screen, pixel_font, asset_manager.images['background'], bird, pipes)
                        else:
                            # Countdown before resuming
                            countdown(screen, pixel_font, bird, pipes, asset_manager.images['background'])

            if not paused:
                bird.update()
                for pipe in pipes:
                    pipe.update()
                    if pipe.off_screen():
                        pipes.remove(pipe)
                        score += 1
                        gap = get_gap(score)
                        pipes.append(Pipe(SCREEN_WIDTH, gap, asset_manager, score))

                    if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                        game_over = True

                if bird.rect.top > SCREEN_HEIGHT:
                    game_over = True

                current_speed = get_speed(score)
                for pipe in pipes:
                    pipe.speed = current_speed

                screen.blit(asset_manager.images['background'], (0, 0))
                bird.draw(screen)
                for pipe in pipes:
                    pipe.draw(screen)

                # Render the score using the pixelated font
                score_surf = pixel_font.render(f'Score: {score}', True, WHITE)
                screen.blit(score_surf, (10, 10))

                pygame.display.flip()
                clock.tick(FPS)

        if not running:
            break

        if score > high_score:
            high_score = score
            save_high_score(high_score)

        menu.draw_game_over(score, high_score, asset_manager.images['background'])

        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_over = False
                        game_started = True
                    if event.key == pygame.K_q:
                        running = False
                        game_over = False

    pygame.quit()

if __name__ == "__main__":
    main()
