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
    elif 61 <= score <= 100:
        return 16
    else:
        return 20

def get_gap(score):
    if score <= 15:
        return 250
    elif 16 <= score <= 40:
        return 240
    elif 41 <= score <= 60:
        return 230
    elif 61 <= score <= 100:
        return 210
    else:
        return 190

def get_level(score):
    if score <= 15:
        return 1
    elif 16 <= score <= 40:
        return 2
    elif 41 <= score <= 60:
        return 3    
    elif 61 <= score <= 100:
        return 4
    else:
        return 5

def load_high_score():
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def save_high_score(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('sounds/background.mp3')
    pygame.mixer.music.set_volume(0.5)  # Set background music volume to 50%
    start_game_over_sound = pygame.mixer.Sound('sounds/start_game_over.mp3')
    start_game_over_sound.set_volume(0.5)  # Set volume to 50%
    game_over_sound = pygame.mixer.Sound('sounds/game_over.mp3')  # Load game over sound
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
    level_start_time = None  # To track the start time of level display

    while running:
        bird = Bird(asset_manager)
        score = 0
        game_over = False

        gap = get_gap(score)
        pipes = [Pipe(SCREEN_WIDTH + i * (70 + gap), gap, asset_manager, score) for i in range(3)]

        menu = Menu(screen, pixel_font)  # Use the pixelated font for the menu
        if initial_start:
            menu.draw_start(asset_manager.images['background'])
            start_game_over_sound.play()  # Play the start game over sound

        while not game_started:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_started = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_started = True
                        initial_start = False
                        pygame.mixer.music.play(-1)  # Start playing the background music
                        start_game_over_sound.stop()  # Stop playing the start game over sound

        current_level = get_level(score)
        level_start_time = pygame.time.get_ticks()  # Start the level display timer

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
                            menu.draw_pause_message_with_neon(asset_manager.images['background'], bird, pipes)
                        else:
                            # Countdown before resuming with neon effect
                            menu.draw_countdown_with_neon(asset_manager.images['background'], bird, pipes)

            if not paused:
                bird.update()
                for pipe in pipes:
                    pipe.update()
                    if pipe.off_screen():
                        pipes.remove(pipe)
                        score += 1
                        gap = get_gap(score)
                        pipes.append(Pipe(SCREEN_WIDTH, gap, asset_manager, score))

                    # Check for pixel-perfect collision using the get_collision method
                    if pipe.get_collision(bird):
                        game_over = True
                        pygame.mixer.music.stop()  # Stop playing the background music
                        start_game_over_sound.play()  # Play the start game over sound
                        game_over_sound.play()  # Play the game over sound

                if bird.rect.top > SCREEN_HEIGHT:
                    game_over = True
                    pygame.mixer.music.stop()  # Stop playing the background music
                    start_game_over_sound.play()  # Play the start game over sound
                    game_over_sound.play()  # Play the game over sound

                current_speed = get_speed(score)
                for pipe in pipes:
                    pipe.speed = current_speed

                screen.blit(asset_manager.images['background'], (0, 0))
                bird.draw(screen)
                for pipe in pipes:
                    pipe.draw(screen)

                # Render the score using the pixelated font
                menu.draw_score(score)

                # Check if the level has changed
                new_level = get_level(score)
                if new_level != current_level:
                    current_level = new_level
                    level_start_time = pygame.time.get_ticks()

                # Display the level text for 3 seconds
                if level_start_time and pygame.time.get_ticks() - level_start_time < 3000:
                    level_text = f'Level {current_level}'
                    level_surface = pixel_font.render(level_text, True, WHITE)
                    level_rect = level_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                    screen.blit(level_surface, level_rect)

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
                        pygame.mixer.music.play(-1)  # Start playing the background music again
                        start_game_over_sound.stop()  # Stop playing the start game over sound
                        game_over_sound.stop()  # Stop playing the game over sound
                    if event.key == pygame.K_q:
                        running = False
                        game_over = False

    pygame.quit()

if __name__ == "__main__":
    main()
